from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json

class InvalidInputError(Exception):
    '''Invalid model input.'''


class WeatherDataRequestSchema(Schema):
    #list vars here
    datetime_converted = fields.Str()
    CloudAmount = fields.Integer()
    Pressure_msl_hpa = fields.Float()
    RelativeHumidity_percent = fields.Float()
    PrecipitationIntensity_mm_h = fields.Float()
    AirTemperature_degC = fields.Float()
    DewPointTemperature_degC = fields.Float()
    WindDirection = fields.Integer()
    GustSpeed_m_s = fields.Float()
    WindSpeed_m_s = fields.Float()
    GlobalRadiation_W_m2 = fields.Float()
    Energy_kWh = fields.Float(allow_none=True)

def _filter_error_rows(errors: dict,
                        validated_input: t.List[dict]
                        ) -> t.List[dict]:
    '''Remove input data rows with errors'''

    indexes=errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input

def validate_inputs(input_data, csv_origin=True):
    '''Check prediction inputs against the schema'''

    # set many=True to allow passing in a list
    # with the 3.3 upgrade of marshmallow all schemas are strict
    schema = WeatherDataRequestSchema(many=True)

    errors = None
    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
