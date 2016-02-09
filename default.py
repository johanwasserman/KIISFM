#!/usr/bin/env python

from os.path import join
from sys import argv
from time import gmtime, strftime, strptime
from urllib import quote_plus, urlopen
from urlparse import parse_qs, urlparse
from xml.dom.minidom import parseString
from xbmc import translatePath
import xbmcaddon
from xbmcgui import Dialog, ListItem, lock, unlock
from xbmcplugin import addDirectoryItem, endOfDirectory

Addon = xbmcaddon.Addon("plugin.audio.kiisfm")

icons = {
	0: join(Addon.getAddonInfo('path'), 'icon.png'),
	1: join(Addon.getAddonInfo('path'), 'resources', 'media', 'ReleaseFM.png'),
}


def config():
	global streams

	# urls
	streams = {
		1: 'http://kiis-fm.akacast.akamaistream.net/7/572/19773/v1/auth.akacast.akamaistream.net/kiis-fm',
	}


def index():
	global icons, streams

	# add items
	addLink('KIIS-FM', streams[1], icons[1], {
		'title': 'KIIS-FM',
	})


def addLink(name, url, image = '', info = {}, totalItems = 0):
	name = name.encode('utf-8')
	item = ListItem(name, iconImage = image, thumbnailImage = image)
	item.setProperty('mimetype', 'audio/mpeg')
	item.setInfo('music', info)
	return addDirectoryItem(int(argv[1]), url, item, False, totalItems)


# get config
config()

# show index
index()

# end menu
endOfDirectory(int(argv[1]))
