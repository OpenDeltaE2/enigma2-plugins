from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
import gettext

PluginLanguageDomain = "AudioSync"
PluginLanguagePath = "Extensions/AudioSync/locale"


def localeInit():
	gettext.bindtextdomain(PluginLanguageDomain, resolveFilename(SCOPE_PLUGINS, PluginLanguagePath))


def _(txt):
	t = gettext.dgettext(PluginLanguageDomain, txt)
	if t == txt:
		#print "[" + PluginLanguageDomain + "] fallback to default translation for ", txt
		t = gettext.gettext(txt)
	return t


localeInit()
language.addCallback(localeInit)
