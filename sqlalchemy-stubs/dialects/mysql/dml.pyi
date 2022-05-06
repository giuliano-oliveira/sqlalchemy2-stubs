from typing import Any

from ... import util as util
from ...sql.dml import Insert as StandardInsert
from ...sql.elements import ClauseElement

class Insert(StandardInsert):
    stringify_dialect: str = ...
    @property
    def inserted(self): ...
    @util.memoized_property
    def inserted_alias(self): ...
    def on_duplicate_key_update(self, *args: Any, **kw: Any) -> "Insert": ...

insert: Any

class OnDuplicateClause(ClauseElement):
    __visit_name__: str = ...
    stringify_dialect: str = ...
    inserted_alias: Any = ...
    update: Any = ...
    def __init__(self, inserted_alias: Any, update: Any) -> None: ...
