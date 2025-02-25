#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Defines the User API routes for the FastAPI application.
"""

import logging

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import ORJSONResponse
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import Response

from src.core.custom_exceptions import ConflictException, \
    InternalServerException, NotFoundException
from src.core.env_config import get_settings
from src.db.connectors.postgres_db import get_pg_db
from src.db.models.v1_models.users_model import UserModel
from src.db.schemas.v1_schemas.user_schemas import UserCreate, UserOutput

# Initialize the API router
router = APIRouter()

# Initialize environment settings & logger
settings = get_settings()
logger = logging.getLogger(
    settings.app_logger_name or "application_logger")


@router.options("", operation_id="options_v1_user_routes")
def options_user_routes() -> Response:
    """
    Handles OPTIONS requests for the /users endpoint.
    """
    return Response(
        status_code=status.HTTP_204_NO_CONTENT,
        headers={"Allow": "GET, POST, PUT, PATCH, DELETE"}
    )


@router.post("",
             name="create_user_v1_in_pg_db",
             description="Create a new User",
             operation_id="create_user_v1_in_pg_db",
             response_class=ORJSONResponse,
             status_code=status.HTTP_201_CREATED)
async def create_user(
        user: UserCreate,
        db: AsyncSession = Depends(get_pg_db)) -> ORJSONResponse:
    """
    Create a new User.
    """
    try:
        new_user = UserModel(**user.dict())
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return ORJSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=UserOutput.model_validate(new_user).model_dump()
        )
    except IntegrityError as e:
        await db.rollback()
        raise ConflictException(
            message="User with given details already exists") from e
    except Exception as e:
        await db.rollback()
        logger.error("Unexpected error occurred: %s", e, exc_info=True)
        raise InternalServerException(message="Internal Server Error") from e


@router.get("",
            response_class=ORJSONResponse,
            operation_id="get_all_users_v1_in_pg_db")
async def get_all_users(
        db: AsyncSession = Depends(get_pg_db)) -> ORJSONResponse:
    """
    Retrieve all Users that are not soft-deleted.
    """
    try:
        async with db as session:
            result = await session.execute(
                select(UserModel)
                .options()
                .filter(UserModel.deleted_at.is_(None))
            )

            if users := result.unique().scalars().all():
                return ORJSONResponse(
                    status_code=status.HTTP_200_OK,
                    content=[UserOutput.model_validate(user).model_dump() for
                             user in users]
                )

            raise NotFoundException(message="No users found")
    except NotFoundException as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        ) from e
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal Server Error"
        ) from e
