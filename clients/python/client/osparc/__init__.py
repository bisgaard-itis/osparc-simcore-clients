"""
0.5.0 osparc client
"""
from ._info import openapi

from osparc_client import (
    __version__,

    # APIs
    FilesApi,
    MetaApi,
    SolversApi,
    StudiesApi,
    UsersApi,

    # API client
    ApiClient,
    Configuration,
    OpenApiException,
    ApiTypeError,
    ApiValueError,
    ApiKeyError,
    ApiException,

    # models
    BodyUploadFileV0FilesContentPut,
    ErrorGet,
    File,
    Groups,
    HTTPValidationError,
    Job,
    JobInputs,
    JobMetadata,
    JobMetadataUpdate,
    JobOutputs,
    JobStatus,
    LimitOffsetPageFile,
    LimitOffsetPageJob,
    LimitOffsetPageSolver,
    LimitOffsetPageStudy,
    Links,
    Meta,
    OnePageSolverPort,
    OnePageStudyPort,
    Profile,
    ProfileUpdate,
    Solver,
    SolverPort,
    Study,
    StudyPort,
    UserRoleEnum,
    UsersGroup,
    ValidationError,
)

from osparc_client import RunningState as TaskStates

__all__ = [
    # imports from osparc_client
    "__version__",
    "FilesApi",
    "MetaApi",
    "SolversApi",
    "UsersApi",
    "BodyUploadFileV0FilesContentPut",
    "File",
    "Groups",
    "HTTPValidationError",
    "Job",
    "JobInputs",
    "JobOutputs",
    "JobStatus",
    "Meta",
    "Profile",
    "ProfileUpdate",
    "Solver",
    "TaskStates",
    "UserRoleEnum",
    "UsersGroup",
    "ValidationError",
    "ApiClient",
    "Configuration",
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiException",
    "StudiesApi",
    "OnePageSolverPort",
    "StudyPort",
    "Study",
    "LimitOffsetPageStudy",
    "LimitOffsetPageFile",
    "JobMetadataUpdate",
    "LimitOffsetPageJob",
    "Links",
    "SolverPort",
    "JobMetadata",
    "LimitOffsetPageSolver",
    "ErrorGet",
    "OnePageStudyPort",
    # imports from osparc
    "openapi",
]
