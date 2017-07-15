from app.models.lic import Lic
from app.models.user import User

from app import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        model = User
        exclude = ["id"]


user_schema = UserSchema()


class LicSchema(ma.ModelSchema):
    class Meta:
        model = Lic
        fields = ["name", "serial", "support_date"]


class LicSchemaLight(ma.ModelSchema):
    class Meta:
        model = Lic
        fields = ["name", "serial"]


lic_schema = LicSchema()
lic_schema_light = LicSchemaLight()
lic_schemas = LicSchema(many=True)
