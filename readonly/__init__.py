from readonly.cursor import (
	_is_readonly,
	PatchedCursorWrapper,
	PatchedCursorDebugWrapper,
)

from django.db.backends import utils


if _is_readonly():
	# Monkey Patching!
	utils.CursorWrapper = PatchedCursorWrapper
	utils.CursorDebugWrapper = PatchedCursorDebugWrapper
