# Some errors occur for the test suite itself, and cannot be addressed via django-stubs. They should be ignored
# using this constant.
import re

IGNORED_MODULES = {'schema', 'gis_tests', 'admin_widgets', 'admin_filters', 'migrations',
                   'sitemaps_tests', 'staticfiles_tests', 'modeladmin', 'model_forms',
                   'generic_views', 'forms_tests', 'flatpages_tests', 'admin_utils',
                   'admin_ordering', 'admin_changelist', 'admin_views', 'mail', 'redirects_tests',
                   'invalid_models_tests', 'i18n', 'migrate_signals', 'model_formsets',
                   'template_tests', 'template_backends', 'test_runner', 'admin_scripts',
                   'sites_tests', 'inline_formsets', 'foreign_object', 'cache', 'test_client', 'test_client_regress'}

MOCK_OBJECTS = ['MockRequest', 'MockCompiler', 'modelz', 'call_count', 'call_args_list',
                'call_args', 'MockUser', 'Xtemplate', 'DummyRequest', 'DummyUser', 'MinimalUser', 'DummyNode']
EXTERNAL_MODULES = ['psycopg2', 'PIL', 'selenium', 'oracle', 'mysql', 'sqlite3', 'sqlparse', 'tblib', 'numpy',
                    'bcrypt', 'argon2', 'xml.dom']
IGNORED_ERRORS = {
    '__common__': [
        *MOCK_OBJECTS,
        *EXTERNAL_MODULES,
        'Need type annotation for',
        'has no attribute "getvalue"',
        'Cannot assign to a method',
        'already defined',
        'Cannot assign to a type',
        '"HttpResponseBase" has no attribute',
        '"object" has no attribute',
        re.compile(r'"Callable\[.+, Any\]" has no attribute'),
        'has no attribute "deconstruct"',
        # private members
        re.compile(r'has no attribute ("|\')_[a-zA-Z_]+("|\')'),
        "'Settings' object has no attribute",
        '**Dict',
        re.compile(r"Expression of type '.*' is not supported"),
        'has incompatible type "object"',
        'undefined in superclass',
        'Argument after ** must be a mapping',
        'note:',
        re.compile(r'Item "None" of "[a-zA-Z_ ,\[\]]+" has no attribute'),
        '"Optional[List[_Record]]"',
        '"Callable[..., None]" has no attribute',
        'does not return a value',
        'has no attribute "alternatives"',
        'gets multiple values for keyword argument',
        '"Handler" has no attribute',
        'Module has no attribute',
        'namedtuple',
        # TODO: see test in managers/test_managers.yml
        "Cannot determine type of",
        'cache_clear',
        'cache_info',
        'Incompatible types in assignment (expression has type "None", variable has type Module)',
        "Module 'django.contrib.messages.storage.fallback' has no attribute 'CookieStorage'",
        # TODO: not supported yet
        'GenericRelation',
        'RelatedObjectDoesNotExist',
        re.compile(r'"Field\[Any, Any\]" has no attribute '
                   r'"(through|field_name|field|get_related_field|related_model|related_name'
                   r'|get_accessor_name|empty_strings_allowed|many_to_many)"'),
        # TODO: multitable inheritance
        'ptr',
        'Incompatible types in assignment (expression has type "Callable[',
        'SimpleLazyObject',
        'Test',
        'Mixin" has no attribute',
        'Incompatible types in string interpolation',
        '"None" has no attribute',
        'has no attribute "assert',
    ],
    'aggregation': [
        re.compile(r'got "Optional\[(Author|Publisher)\]", expected "Union\[(Author|Publisher), Combinable\]"'),
        'Argument 2 for "super" not an instance of argument 1',
    ],
    'annotations': [
        'Incompatible type for "store" of "Employee" (got "Optional[Store]", expected "Union[Store, Combinable]")'
    ],
    'apps': [
        'Incompatible types in assignment (expression has type "str", target has type "type")',
    ],
    'auth_tests': [
        '"PasswordValidator" has no attribute "min_length"',
        'AbstractBaseUser',
        'Argument "password_validators" to "password_changed" has incompatible type "Tuple[Validator]"; '
        + 'expected "Optional[Sequence[PasswordValidator]]"',
        'Unsupported right operand type for in ("object")',
        'mock_getpass',
        'Unsupported left operand type for + ("Sequence[str]")',
        'AuthenticationFormWithInactiveUsersOkay',
        'Incompatible types in assignment (expression has type "Dict[str, Any]", variable has type "QueryDict")',
        'No overload variant of "int" matches argument type "AnonymousUser"',
        'expression has type "AnonymousUser", variable has type "User"',
    ],
    'basic': [
        'Unexpected keyword argument "unknown_kwarg" for "refresh_from_db" of "Model"',
        'Unexpected attribute "foo" for model "Article"',
        'has no attribute "touched"',
        'Incompatible types in assignment (expression has type "Type[CustomQuerySet]"',
        '"Manager[Article]" has no attribute "do_something"',
    ],
    'backends': [
        '"DatabaseError" has no attribute "pgcode"'
    ],
    'builtin_server': [
        '"ServerHandler" has no attribute',
    ],
    'bulk_create': [
        'has incompatible type "List[Country]"; expected "Iterable[TwoFields]"',
        'List item 1 has incompatible type "Country"; expected "ProxyCountry"',
    ],
    'check_framework': [
        'base class "Model" defined the type as "Callable',
        'Value of type "Collection[str]" is not indexable',
        'Unsupported target for indexed assignment',
    ],
    'constraints': [
        'Argument "condition" to "UniqueConstraint" has incompatible type "str"; expected "Optional[Q]"'
    ],
    'contenttypes_tests': [
        '"FooWithBrokenAbsoluteUrl" has no attribute "unknown_field"',
        'contenttypes_tests.models.Site',
        'Argument 1 to "set" of "RelatedManager" has incompatible type "SiteManager[Site]"',
    ],
    'custom_lookups': [
        'in base class "SQLFuncMixin"',
        'has no attribute "name"',
    ],
    'custom_columns': [
        "Cannot resolve keyword 'firstname' into field",
    ],
    'custom_pk': [
        '"Employee" has no attribute "id"',
    ],
    'custom_managers': [
        'Unsupported dynamic base class',
        'Incompatible types in assignment (expression has type "CharField',
        'Item "Book" of "Optional[Book]" has no attribute "favorite_avg"',
    ],
    'csrf_tests': [
        'expression has type "property", base class "HttpRequest" defined the type as "QueryDict"',
        'expression has type "Dict[<nothing>, <nothing>]", variable has type "SessionBase"',
    ],
    'dates': [
        'Too few arguments for "dates" of',
    ],
    'dbshell': [
        'Incompatible types in assignment (expression has type "None"',
    ],
    'defer': [
        'Too many arguments for "refresh_from_db" of "Model"'
    ],
    'delete': [
        'Incompatible type for lookup \'pk\': (got "Optional[int]", expected "Union[str, int]")',
    ],
    'dispatch': [
        'Item "str" of "Union[ValueError, str]" has no attribute "args"'
    ],
    'deprecation': [
        '"Manager" has no attribute "old"',
        '"Manager" has no attribute "new"'
    ],
    'db_functions': [
        '"FloatModel" has no attribute',
        'Incompatible types in assignment (expression has type "Optional[Any]", variable has type "FloatModel")'
    ],
    'decorators': [
        '"Type[object]" has no attribute "method"'
    ],
    'expressions_case': [
        'Item "Field[Any, Any]" of "Union[Field[Any, Any], ForeignObjectRel]" has no attribute "is_relation"'
    ],
    'expressions_window': [
        'has incompatible type "str"'
    ],
    'file_uploads': [
        'has no attribute "content_type"',
    ],
    'file_storage': [
        'Incompatible types in assignment (expression has type "None", variable has type "str")',
        'Property "base_url" defined in "FileSystemStorage" is read-only',
    ],
    'files': [
        'Incompatible types in assignment (expression has type "IOBase", variable has type "File")',
        'Argument 1 to "write" of "SpooledTemporaryFile"',
    ],
    'filtered_relation': [
        'has no attribute "name"',
    ],
    'fixtures': [
        'Incompatible types in assignment (expression has type "int", target has type "Iterable[str]")',
        'Incompatible types in assignment (expression has type "SpyManager[Spy]"',
    ],
    'fixtures_regress': [
        'Unsupported left operand type for + ("None")',
    ],
    'from_db_value': [
        '"Cash" has no attribute',
        'Argument 1 to "__str__" of "Decimal"',
    ],
    'get_object_or_404': [
        'Argument 1 to "get_object_or_404" has incompatible type "str"; '
        + 'expected "Union[Type[<nothing>], QuerySet[<nothing>]]"',
        'Argument 1 to "get_list_or_404" has incompatible type "List[Type[Article]]"; '
        + 'expected "Union[Type[<nothing>], QuerySet[<nothing>]]"',
        'CustomClass',
    ],
    'generic_relations': [
        "Cannot resolve keyword 'vegetable' into field",
    ],
    'generic_relations_regress': [
        '"Link" has no attribute',
    ],
    'httpwrappers': [
        'Argument 2 to "appendlist" of "QueryDict"',
        'Incompatible types in assignment (expression has type "int", target has type "Union[str, List[str]]")',
        'Argument 1 to "fromkeys" of "QueryDict" has incompatible type "int"',
    ],
    'humanize_tests': [
        'Argument 1 to "append" of "list" has incompatible type "None"; expected "str"',
    ],
    'lookup': [
        'Unexpected keyword argument "headline__startswith" for "in_bulk" of',
        'is called with more than one field',
        "Cannot resolve keyword 'pub_date_year' into field",
        "Cannot resolve keyword 'blahblah' into field",
    ],
    'logging_tests': [
        re.compile(r'Argument [0-9] to "makeRecord" of "Logger"'),
        '"LogRecord" has no attribute "request"',
    ],
    'm2m_regress': [
        "Cannot resolve keyword 'porcupine' into field",
        'Argument 1 to "set" of "RelatedManager" has incompatible type "int"',
    ],
    'messages_tests': [
        'List item 0 has incompatible type "Dict[str, Message]"; expected "Message"',
        'Too many arguments',
        'CustomRequest',
    ],
    'middleware': [
        re.compile(r'"(HttpRequest|WSGIRequest)" has no attribute'),
    ],
    'many_to_many': [
        '(expression has type "List[Article]", variable has type "RelatedManager[Article]"',
        '"add" of "RelatedManager" has incompatible type "Article"; expected "Union[Publication, int]"',
    ],
    'many_to_one': [
        'Incompatible type for "parent" of "Child" (got "None", expected "Union[Parent, Combinable]")',
        'Incompatible type for "parent" of "Child" (got "Child", expected "Union[Parent, Combinable]")',
        'expression has type "List[<nothing>]", variable has type "RelatedManager[Article]"',
        '"Reporter" has no attribute "cached_query"',
        'to "add" of "RelatedManager" has incompatible type "Reporter"; expected "Union[Article, int]"',
    ],
    'middleware_exceptions': [
        'Argument 1 to "append" of "list" has incompatible type "Tuple[Any, Any]"; expected "str"'
    ],
    'model_fields': [
        'Item "Field[Any, Any]" of "Union[Field[Any, Any], ForeignObjectRel]" has no attribute',
        'Incompatible types in assignment (expression has type "Type[Person',
        'Incompatible types in assignment (expression has type "FloatModel", variable has type',
        'No overload variant of "bytes" matches argument type "Container[int]"',
        '"ImageFile" has no attribute "was_opened"',
    ],
    'model_indexes': [
        'Argument "condition" to "Index" has incompatible type "str"; expected "Optional[Q]"'
    ],
    'model_inheritance': [
        'base class "AbstractBase" defined',
        'base class "AbstractModel" defined',
        'Definition of "name" in base class "ConcreteParent"',
        ' Definition of "name" in base class "AbstractParent"',
        'referent_references',
        "Cannot resolve keyword 'attached_comment_set' into field"
    ],
    'model_meta': [
        'List item 0 has incompatible type "str"; expected "Union[Field[Any, Any], ForeignObjectRel]"'
    ],
    'model_regress': [
        'Incompatible type for "department" of "Worker"',
        '"PickledModel" has no attribute',
        '"Department" has no attribute "evaluate"',
    ],
    'model_formsets_regress': [
        'Incompatible types in assignment (expression has type "int", target has type "str")',
    ],
    'model_options': [
        'expression has type "Dict[str, Type[Model]]", target has type "OrderedDict',
    ],
    'multiple_database': [
        'Unexpected attribute "extra_arg" for model "Book"'
    ],
    'null_queries': [
        "Cannot resolve keyword 'foo' into field"
    ],
    'order_with_respect_to': [
        '"Dimension" has no attribute "set_component_order"',
    ],
    'one_to_one': [
        'expression has type "None", variable has type "UndergroundBar"',
        'Item "OneToOneField[Union[Place, Combinable], Place]" '
        + 'of "Union[OneToOneField[Union[Place, Combinable], Place], Any]"',
    ],
    'pagination': [
        '"int" not callable',
    ],
    'postgres_tests': [
        'DummyArrayField',
        'DummyJSONField',
        'Incompatible types in assignment (expression has type "Type[Field[Any, Any]]',
        'Argument "encoder" to "JSONField" has incompatible type "DjangoJSONEncoder";',
        '("None" and "SearchQuery")',
    ],
    'properties': [
        re.compile('Unexpected attribute "(full_name|full_name_2)" for model "Person"')
    ],
    'prefetch_related': [
        '"Person" has no attribute "houses_lst"',
        '"Book" has no attribute "first_authors"',
        '"Book" has no attribute "the_authors"',
        'Incompatible types in assignment (expression has type "List[Room]", variable has type "Manager[Room]")',
        'Item "Room" of "Optional[Room]" has no attribute "house_attr"',
        'Item "Room" of "Optional[Room]" has no attribute "main_room_of_attr"',
        'Argument 2 to "Prefetch" has incompatible type "ValuesQuerySet'
    ],
    'proxy_models': [
        'Incompatible types in assignment',
        'in base class "User"'
    ],
    'queries': [
        'Incompatible types in assignment (expression has type "None", variable has type "str")',
        'Invalid index type "Optional[str]" for "Dict[str, int]"; expected type "str"',
        'Unsupported operand types for & ("Manager[Author]" and "Manager[Tag]")',
        'Unsupported operand types for | ("Manager[Author]" and "Manager[Tag]")',
        'ObjectA',
        "'flat' and 'named' can't be used together",
        '"Collection[Any]" has no attribute "explain"',
        "Cannot resolve keyword 'unknown_field' into field",
        'Incompatible type for lookup \'tag\': (got "str", expected "Union[Tag, int, None]")',
    ],
    'requests': [
        'Incompatible types in assignment (expression has type "Dict[str, str]", variable has type "QueryDict")'
    ],
    'responses': [
        'Argument 1 to "TextIOWrapper" has incompatible type "HttpResponse"; expected "IO[bytes]"'
    ],
    'reverse_lookup': [
        "Cannot resolve keyword 'choice' into field"
    ],
    'settings_tests': [
        'Argument 1 to "Settings" has incompatible type "Optional[str]"; expected "str"'
    ],
    'signals': [
        'Argument 1 to "append" of "list" has incompatible type "Tuple[Any, Any, Optional[Any], Any]";'
    ],
    'sites_framework': [
        'expression has type "CurrentSiteManager[CustomArticle]", base class "AbstractArticle"'
    ],
    'syndication_tests': [
        'List or tuple expected as variable arguments'
    ],
    'sessions_tests': [
        'Incompatible types in assignment (expression has type "None", variable has type "int")',
        '"AbstractBaseSession" has no attribute',
        '"None" not callable',
    ],
    'select_related': [
        'Item "ForeignKey[Union[Genus, Combinable], Genus]" '
        + 'of "Union[ForeignKey[Union[Genus, Combinable], Genus], Any]"'
    ],
    'select_related_onetoone': [
        'Incompatible types in assignment (expression has type "Parent2", variable has type "Parent1")',
        '"Parent1" has no attribute'
    ],
    'servers': [
        re.compile('Argument [0-9] to "WSGIRequestHandler"'),
        '"HTTPResponse" has no attribute',
        '"type" has no attribute',
        '"WSGIRequest" has no attribute "makefile"',
        'LiveServerAddress',
        '"Stub" has no attribute "makefile"',
    ],
    'serializers': [
        '"Model" has no attribute "data"',
        '"Iterable[Any]" has no attribute "content"',
        re.compile(r'Argument 1 to "(serialize|deserialize)" has incompatible type "None"; expected "str"')
    ],
    'string_lookup': [
        '"Bar" has no attribute "place"',
    ],
    'test_utils': [
        '"PossessedCar" has no attribute "color"',
        'expression has type "None", variable has type "List[str]"',
    ],
    'transactions': [
        'Incompatible types in assignment (expression has type "Thread", variable has type "Callable[[], Any]")'
    ],
    'urlpatterns': [
        '"object" not callable',
        '"None" not callable',
    ],
    'urlpatterns_reverse': [
        'List or tuple expected as variable arguments',
        'No overload variant of "zip" matches argument types "Any", "object"',
        'Argument 1 to "get_callable" has incompatible type "int"'
    ],
    'utils_tests': [
        'Argument 1 to "activate" has incompatible type "None"; expected "Union[tzinfo, str]"',
        'Argument 1 to "activate" has incompatible type "Optional[str]"; expected "str"',
        'Incompatible types in assignment (expression has type "None", base class "object" defined the type as',
        'Class',
        'has no attribute "cp"',
        'Argument "name" to "cached_property" has incompatible type "int"; expected "Optional[str]"',
        'has no attribute "sort"',
        'Unsupported target for indexed assignment',
        'defined the type as "None"',
        'Argument 1 to "Path" has incompatible type "Optional[str]"',
        '"None" not callable',
        '"WSGIRequest" has no attribute "process_response_content"',
        'No overload variant of "join" matches argument types "str", "None"',
        'Argument 1 to "Archive" has incompatible type "None"; expected "str"',

    ],
    'view_tests': [
        "Module 'django.views.debug' has no attribute 'Path'",
        'Value of type "Optional[List[str]]" is not indexable',
        'ExceptionUser',
        'view_tests.tests.test_debug.User',
    ],
    'validation': [
        'has no attribute "name"',
    ],
}


def check_if_custom_ignores_are_covered_by_common() -> None:
    from scripts.typecheck_tests import is_pattern_fits

    common_ignore_patterns = IGNORED_ERRORS['__common__']
    for module_name, patterns in IGNORED_ERRORS.items():
        if module_name == '__common__':
            continue
        for pattern in patterns:
            for common_pattern in common_ignore_patterns:
                if isinstance(pattern, str) and is_pattern_fits(common_pattern, pattern):
                    print(f'pattern "{module_name}: {pattern!r}" is covered by pattern {common_pattern!r}')


check_if_custom_ignores_are_covered_by_common()
