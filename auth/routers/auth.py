from fastapi import APIRouter

app = APIRouter(tags=["Auth"])


# @app.post("/auth/signup", status_code=201)
# async def create_user(
#     response: Response,
#     user: auth_schemas.UserCreate,
#     background_tasks: BackgroundTasks,
#     db: orm.Session = fastapi.Depends(get_db),
# ):

#     """intro-->This endpoint allows creation of a new user. To create a new user, you need to send a post request to the /auth/signup endpoint with a body of request containing details of the new user.
#     paramDesc-->

#         reqBody-->email: This is the email of the new user.
#         reqBody-->password: This is the unique password of the new user .
#         reqBody-->first_name: This is the first name of the new user.
#         reqBody-->last_name: This is the last name of the new user.
#         reqBody-->phone_number: This is the phone number of the new user.
#         reqBody-->country_code: This is the country code of the new user.
#         reqBody-->image: This is an image file of the new user, can be of any format.
#         reqBody-->device_id: This is the id of the device used at signup.
#         reqBody-->country: This is the country name of the new user.
#         reqBody-->state: This is the state name of the new user.
#         reqBody-->google_id: This is a unique id of the new user's google account.
#         reqBody-->google_image: This is the image of the user's google account.

#     returnDesc-->On sucessful request, it returns
#         returnBody-->
#             data: The newly created user.
#             access_token: An access token for the user that lasts 15 mins
#             refresh_token: A refresh token for the user that lasts three days.
#     """

#     new_user = await auth_service.create_user(user=user, db=db)
#     print(new_user)
#     print(new_user.__dict__)
#     if new_user is not None:
#         access_token = await auth_service.create_access_token(
#             data={"user_id": new_user.id}, db=db
#         )

#         refresh_token = await auth_service.create_refresh_token(
#             data={"user_id": new_user.id}, db=db
#         )

#         slack_notif_data = {
#             'blocks': signup_block(new_user, signup_type='auth'),
#             #'text': f'New signup from {new_user.first_name} {new_user.last_name}\nEmail: {new_user.email}\nPhone: {new_user.phone_country_code}{new_user.phone_number}',
#             'channel': f"{config('SLACK_SIGNUP_CHANNEL')}",
#         }

#         if (config('PYTHON_ENV') != "development"):
#             background_tasks.add_task(
#                 Helpers.send_slack_notification, config("SLACK_SIGNUP_WEBHOOK_URL"), slack_notif_data
#             )

#         response.set_cookie(
#             key="refresh_token",
#             value=refresh_token,
#             max_age=REFRESH_TOKEN_EXPIRY,
#             secure=IS_REFRESH_TOKEN_SECURE,
#             httponly=True,
#             samesite="strict",
#         )

#         new_user.has_password = True if new_user.password_hash is not None else False

#         response_data = {
#             "data": users_schemas.UserCreateOut.from_orm(new_user),
#             "access_token": access_token,
#             "refresh_token": refresh_token
#         }
#         if user.device_id is not None:
#             device_token = await auth_service.create_device_token(user, db)
#             response_data.update({
#                 "device_id": user.device_id, "device_token": device_token.token
#             })

#         return response_data
