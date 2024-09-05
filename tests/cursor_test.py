from readonly.cursor import _is_readonly, _get_readonly_dbs


def test__is_readonly(settings):
	delattr(settings, "SITE_READ_ONLY")
	assert not _is_readonly()

	settings.SITE_READ_ONLY = False
	assert not _is_readonly()

	settings.SITE_READ_ONLY = True
	assert _is_readonly()


def test__get_readonly_dbs(settings):
	delattr(settings, "DB_READ_ONLY_DATABASES")
	assert _get_readonly_dbs() == []

	settings.DB_READ_ONLY_DATABASES = []
	assert _get_readonly_dbs() == []

	settings.DATABASES = {
		"default": {
			"NAME": "NAME-default",
		},
		"db1": {
			"NAME": "NAME-db1",
		},
		"db2": {
			"NAME": "NAME-db2",
		},
		"db3": {
			"NAME": "NAME-db3",
		},
	}
	settings.DB_READ_ONLY_DATABASES = ["default", "db2"]
	assert _get_readonly_dbs() == ["default", "db2"]
