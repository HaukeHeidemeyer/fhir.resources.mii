# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/StructureDefinition/DetectedIssue
Release: STU3
Version: 3.0.2
Revision: 11917
Last updated: 2019-10-24T11:53:00+11:00
"""
import typing

from pydantic import Field, root_validator
from pydantic.error_wrappers import ErrorWrapper, ValidationError
from pydantic.errors import MissingError, NoneIsNotAllowedError

from . import backboneelement, domainresource, fhirtypes


class DetectedIssue(domainresource.DomainResource):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Clinical issue with action.
    Indicates an actual or potential clinical issue with or between one or more
    active or proposed clinical actions for a patient; e.g. Drug-drug
    interaction, Ineffective treatment frequency, Procedure-condition conflict,
    etc.
    """

    resource_type = Field("DetectedIssue", const=True)

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="The provider or device that identified the issue",
        description=(
            "Individual or device responsible for the issue being raised.  For "
            "example, a decision support application or a pharmacist conducting a "
            "medication review."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner", "Device"],
    )

    category: fhirtypes.CodeableConceptType = Field(
        None,
        alias="category",
        title="Issue Category, e.g. drug-drug, duplicate therapy, etc.",
        description="Identifies the general type of issue identified.",
        # if property is element of this resource.
        element_property=True,
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="When identified",
        description=(
            "The date or date-time when the detected issue was initially " "identified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )

    detail: fhirtypes.String = Field(
        None,
        alias="detail",
        title="Description and context",
        description="A textual explanation of the detected issue.",
        # if property is element of this resource.
        element_property=True,
    )
    detail__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_detail", title="Extension field for ``detail``."
    )

    identifier: fhirtypes.IdentifierType = Field(
        None,
        alias="identifier",
        title="Unique id for the detected issue",
        description="Business identifier associated with the detected issue record.",
        # if property is element of this resource.
        element_property=True,
    )

    implicated: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="implicated",
        title="Problem resource",
        description=(
            "Indicates the resource representing the current activity or proposed "
            "activity that is potentially problematic."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Resource"],
    )

    mitigation: typing.List[fhirtypes.DetectedIssueMitigationType] = Field(
        None,
        alias="mitigation",
        title="Step taken to address",
        description=(
            "Indicates an action that has been taken or is committed to to reduce "
            "or eliminate the likelihood of the risk identified by the detected "
            "issue from manifesting.  Can also reflect an observation of known "
            "mitigating factors that may reduce/eliminate the need for any action."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    patient: fhirtypes.ReferenceType = Field(
        None,
        alias="patient",
        title="Associated patient",
        description=(
            "Indicates the patient whose record the detected issue is associated "
            "with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Patient"],
    )

    reference: fhirtypes.Uri = Field(
        None,
        alias="reference",
        title="Authority for issue",
        description=(
            "The literature, knowledge-base or similar reference that describes the"
            " propensity for the detected issue identified."
        ),
        # if property is element of this resource.
        element_property=True,
    )
    reference__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_reference", title="Extension field for ``reference``."
    )

    severity: fhirtypes.Code = Field(
        None,
        alias="severity",
        title="high | moderate | low",
        description=(
            "Indicates the degree of importance associated with the identified "
            "issue based on the potential impact on the patient."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["high", "moderate", "low"],
    )
    severity__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_severity", title="Extension field for ``severity``."
    )

    status: fhirtypes.Code = Field(
        None,
        alias="status",
        title="registered | preliminary | final | amended +",
        description="Indicates the status of the detected issue.",
        # if property is element of this resource.
        element_property=True,
        element_required=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["registered", "preliminary", "final", "amended", "+"],
    )
    status__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_status", title="Extension field for ``status``."
    )

    @root_validator(pre=True)
    def validate_required_primitive_elements(
        cls, values: typing.Dict[str, typing.Any]
    ) -> typing.Dict[str, typing.Any]:
        """https://www.hl7.org/fhir/extensibility.html#Special-Case
        In some cases, implementers might find that they do not have appropriate data for
        an element with minimum cardinality = 1. In this case, the element must be present,
        but unless the resource or a profile on it has made the actual value of the primitive
        data type mandatory, it is possible to provide an extension that explains why
        the primitive value is not present.
        """
        required_fields = [("status", "status__ext")]
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


class DetectedIssueMitigation(backboneelement.BackboneElement):
    """Disclaimer: Any field name ends with ``__ext`` does't part of
    Resource StructureDefinition, instead used to enable Extensibility feature
    for FHIR Primitive Data Types.

    Step taken to address.
    Indicates an action that has been taken or is committed to to reduce or
    eliminate the likelihood of the risk identified by the detected issue from
    manifesting.  Can also reflect an observation of known mitigating factors
    that may reduce/eliminate the need for any action.
    """

    resource_type = Field("DetectedIssueMitigation", const=True)

    action: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="action",
        title="What mitigation?",
        description=(
            "Describes the action that was taken or the observation that was made "
            "that reduces/eliminates the risk associated with the identified issue."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    author: fhirtypes.ReferenceType = Field(
        None,
        alias="author",
        title="Who is committing?",
        description=(
            "Identifies the practitioner who determined the mitigation and takes "
            "responsibility for the mitigation step occurring."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["Practitioner"],
    )

    date: fhirtypes.DateTime = Field(
        None,
        alias="date",
        title="Date committed",
        description="Indicates when the mitigating action was documented.",
        # if property is element of this resource.
        element_property=True,
    )
    date__ext: fhirtypes.FHIRPrimitiveExtensionType = Field(
        None, alias="_date", title="Extension field for ``date``."
    )
