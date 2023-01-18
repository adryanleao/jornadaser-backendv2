from app.controllers.base_crud import CRUDBase

from .. import models
from .. import schemas

# Creating a new instance of CRUDBase class.
crud_city = CRUDBase(models.City, schemas.CitySchema)
crud_country = CRUDBase(models.Country, schemas.CountrySchema)
crud_group = CRUDBase(models.Group, schemas.GroupSchema)
crud_state = CRUDBase(models.State, schemas.StateSchema)
crud_user_address = CRUDBase(models.UserAddress, schemas.AddressSchema)
crud_community = CRUDBase(models.Community, schemas.CommunitySchema)
crud_maas = CRUDBase(models.Maas, schemas.MaasSchema)
crud_main_company = CRUDBase(models.MainCompany, schemas.MainCompanySchema)
crud_main_settings = CRUDBase(models.MainSettings,
                              schemas.MainSettingsSchema)
crud_extra_material = CRUDBase(models.ExtraMaterial,
                               schemas.ExtraMaterialSchema)
crud_notification = CRUDBase(models.Notification,
                               schemas.NotificationSchema)
crud_secretary_address = CRUDBase(models.SecretaryAddress, schemas.SecretaryAddressSchema)
crud_secretary_maas_rating = CRUDBase(models.SecretaryMaasRating, schemas.SecretaryMaasRatingSchema)
crud_institution_address = CRUDBase(models.InstitutionAddress, schemas.InstitutionAddressSchema)
crud_school_class = CRUDBase(models.SchoolClass, schemas.SchoolClassSchema)
crud_category = CRUDBase(models.Category, schemas.CategorySchema)
crud_week = CRUDBase(models.Week, schemas.WeekSchema)
crud_content = CRUDBase(models.Content, schemas.ContentSchema)