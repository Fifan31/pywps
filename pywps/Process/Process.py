# Author:    Jachym Cepicky
#            http://les-ejk.cz
# License:
#
# Web Processing Service implementation
# Copyright (C) 2006 Jachym Cepicky
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

from pywps.Process import WPSProcess
import sys
print >>sys.stderr, """PyWPS Warning: Usage of"""
print >>sys.stderr, """PyWPS Warning:       from pywps.Process.Process import WPSProcess"""
print >>sys.stderr, """PyWPS Warning: is deprecated. Use """
print >>sys.stderr, """PyWPS Warning:       from pywps.Process import WPSProcess"""
print >>sys.stderr, """PyWPS Warning: instead!"""
