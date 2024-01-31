




# def is_authenticated(
#     token: Union[str, auth_schemas.SUAuth,
#                  auth_schemas.ApiKeyAuth] = Depends(oauth2_scheme),
#     refresh_token: Union[str, None] = Cookie(default=None),
#     db: orm.Session = Depends(get_db),
# ) -> Union[users_schemas.User, JWTError]:

#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     if type(token) == str:
#         access_token = verify_access_token(token, credentials_exception, db)

#         if type(access_token) is JWTError:
#             refresh_token = verify_refresh_token(
#                 refresh_token, credentials_exception, db
#             )

#             user = (
#                 db.query(user_models.User)
#                 .filter(user_models.User.id == refresh_token.id)
#                 .first()
#             )

#             return user

#         if access_token.type == "user":
#             user = (
#                 db.query(user_models.User)
#                 .filter(user_models.User.id == access_token.id)
#                 .first()
#             )

#             return user
#         else:
#             customer = (
#                 db.query(biz_partner_models.Customer).filter(biz_partner_models.Customer.biz_partner_id == access_token.id).first()
#             )

#             return customer

#     if type(token) == auth_schemas.ApiKeyAuth:
#         app_id = token.APP_ID
#         api_key = token.API_KEY
#         user = check_api_key(app_id, api_key, db)

#         return user

#     if type(token) == auth_schemas.SUAuth:
#         user = valid_email_from_db(token.email, db)

#         if (user.is_superuser) == False:
#             raise HTTPException(status_code=403, detail="Unauthorized")

#         return user

#     return JWTError(credentials_exception)