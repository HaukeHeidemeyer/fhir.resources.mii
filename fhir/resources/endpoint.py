# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/Endpoint
Release: R5
Version: 5.0.0
Build ID: 2aecd53
Last updated: 2023-03-26T15:21:02.749+11:00
"""
import typing

from pydantic.v1 import Field, root_validator
from pydantic.v1.error_wrappers import ErrorWrapper, ValidationError
from pydantic.v1.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class Endpoint(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    The technical details of an endpoint that can be used for electronic
    services.
    The technical details of an endpoint that can be used for electronic
    services, such as for web services providing XDS.b, a REST endpoint for
    another FHIR server, or a s/Mime email address. This may include any
    security context information.
    """

    resource_type = Field("Endpoint", const=True)

    address: fhirtypes.Url = Field(
        None,
        alias="address",
        title="The technical base address for connecting to this endpoint",
        description="The uri that describes the actual end-point to connect to.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
    )
    address__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_address", title="Extension field for ``address``."
    )

    connectionType: typing.List[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="connectionType",
        title="Protocol/Profile/Standard to be used with this endpoint connection",
        description=(
            "A coded value that represents the technical details of the usage of "
            "this endpoint, such as what WSDLs should be used in what way. (e.g. "
            "XDS.b/DICOM/cds-hook)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    contact: typing.List[fhirtypes.ContactPointType] = Field(
        None,
        alias="contact",
        title="Contact details for source (e.g. troubleshooting)",
        description=(
            "Contact details for a human to contact about the endpoint. The primary"
            " use of this for system administrator troubleshooting."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    description: fhirtypes.String = Field(
        None,
        alias="description",
        title=(
            "Additional details about the endpoint that could be displayed as "
            "further information to identify the description beyond its name"
        ),
        description=(
            "The description of the endpoint and what it is for (typically used as "
            "supplemental information in an endpoint directory describing its "
            "usage/purpose)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    description__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_description", title="Extension field for ``description``."
    )

    environmentType: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="environmentType",
        title="The type of environment(s) exposed at this endpoint",
        description=(
            "The type of environment(s) exposed at this endpoint (dev, prod, test, "
            "etc.)."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    header: typing.List[typing.Optional[fhirtypes.String]] = Field(
        None,
        alias="header",
        title="Usage depends on the channel type",
        description="Additional headers / information to send as part of the notification.",
        # if property is element of this resource.
        element_property=True,
    )
    header__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_header", title="Extension field for ``header``.")

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        None,
        alias="identifier",
        title="Identifies this endpoint across multiple systems",
        description=(
            "Identifier for the organization that is used to identify the endpoint "
            "across multiple disparate systems."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title=(
            "Organization that manages this endpoint (might not be the organization"
            " that exposes the endpoint)"
        ),
        description=(
            "The organization that manages this endpoint (even if technically "
            "another organization is hosting this in the cloud, it is the "
            "organization associated with the data)."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Organization"],
    )

    name: fhirtypes.String = Field(
        None,
        alias="name",
        title="A name that this endpoint can be identified by",
        description="A friendly name that this endpoint can be referred to with.",
        # if property is element of this resource.
        element_property=True,
    )
    name__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_name", title="Extension field for ``name``."
    )

    payload: typing.List[fhirtypes.EndpointPayloadType] = Field(
        None,
        alias="payload",
        title="Set of payloads that are provided by this endpoint",
        description="The set of payloads that are provided/available at this endpoint.",
        # if property is element of this resource.
        element_property=True,
    )

    period: fhirtypes.PeriodType = Field(
        None,
        alias="period",
        title="Interval the endpoint is expected to be operational",
        description="The interval during which the endpoint is expected to be operational.",
        # if property is element of this resource.
        element_property=True,
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="active | suspended | error | off | entered-in-error | test",
        description=(
            "The endpoint status represents the general expected availability of an"
            " endpoint."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["active", "suspended", "error", "off", "entered-in-error", "test"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``Endpoint`` according specification,
        with preserving original sequence order.
        """
        return [
            "id",
            "meta",
            "implicitRules",
            "language",
            "text",
            "contained",
            "extension",
            "modifierExtension",
            "identifier",
            "status",
            "connectionType",
            "name",
            "description",
            "environmentType",
            "managingOrganization",
            "contact",
            "period",
            "payload",
            "address",
            "header",
        ]

    @root_validator(pre=True, allow_reuse=True)
    def validate_required_primitive_elements_1018(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("address", "address__ext"), ("status", "status__ext")]
        _missing = object()

        def _fallback():
            return ""

        errors: typing.List["ErrorWrapper"] = []
        for name, ext in required_fields:
            field = cls.__fields__[name]
            ext_field = cls.__fields__[ext]
            value = values.get(field.alias, _missing)
            if value not in (_missing, None):
                continue
            ext_value = values.get(ext_field.alias, _missing)
            missing_ext = True
            if ext_value not in (_missing, None):
                if isinstance(ext_value, dict):
                    missing_ext = len(ext_value.get("extension", [])) == 0
                elif (
                    getattr(ext_value.__class__, "get_resource_type", _fallback)()
                    == "FHIRPrimitiveExtension"
                ):
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
                else:
                    validate_pass = True
                    for validator in ext_field.type_.__get_validators__():
                        try:
                            ext_value = validator(v=ext_value)
                        except ValidationError as exc:
                            errors.append(ErrorWrapper(exc, loc=ext_field.alias))
                            validate_pass = False
                    if not validate_pass:
                        continue
                    if ext_value.extension and len(ext_value.extension) > 0:
                        missing_ext = False
            if missing_ext:
                if value is _missing:
                    errors.append(ErrorWrapper(MissingError(), loc=field.alias))
                else:
                    errors.append(
                        ErrorWrapper(NoneIsNotAllowedError(), loc=field.alias)
                    )
        if len(errors) > 0:
            raise ValidationError(errors, cls)  # type: ignore

        return values


class EndpointPayload(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` doesn't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Set of payloads that are provided by this endpoint.
    The set of payloads that are provided/available at this endpoint.
    """

    resource_type = Field("EndpointPayload", const=True)

    mimeType: typing.List[typing.Optional[fhirtypes.Code]] = Field(
        None,
        alias="mimeType",
        title=(
            "Mimetype to send. If not specified, the content could be anything "
            "(including no payload, if the connectionType defined this)"
        ),
        description=(
            "The mime type to send the payload in - e.g. application/fhir+xml, "
            "application/fhir+json. If the mime type is not specified, then the "
            "sender could send any content (including no content depending on the "
            "connectionType)."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    mimeType__ext: typing.List[
        typing.Union[fhirtypes.FHIRPrimitiveExtensionType, None]
    ] = Field(None, alias="_mimeType", title="Extension field for ``mimeType``.")

    type: typing.List[fhirtypes.CodeableConceptType] = Field(
        None,
        alias="type",
        title=(
            "The type of content that may be used at this endpoint (e.g. XDS "
            "Discharge summaries)"
        ),
        description=(
            "The payload type describes the acceptable content that can be "
            "communicated on the endpoint."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    @classmethod
    def elements_sequence(cls):
        """returning all elements names from
        ``EndpointPayload`` according specification,
        with preserving original sequence order.
        """
        return ["id", "extension", "modifierExtension", "type", "mimeType"]
