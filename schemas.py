from flask_marshmallow import Marshmallow
from models import Lic

ma = Marshmallow()


class LicSchema(ma.ModelSchema):
    class Meta:
        model = Lic
        fields = ["name", "serial", "support_date"]


class LicSchemaLight(ma.ModelSchema):
    class Meta:
        model = Lic
        fields = ["name", "support_date"]


lic_schema = LicSchema()
lic_schema_light = LicSchemaLight()