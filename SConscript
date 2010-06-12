# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/AncillaryDataUtil/SConscript,v 1.7 2010/06/11 00:32:49 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataUtil-01-00-05
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

AncillaryDataUtil = libEnv.StaticLibrary('AncillaryDataUtil', listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataUtilLib')
test_AncillaryDataUtil = progEnv.Program('test_AncillaryDataUtil',['src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AncillaryDataUtil',
             libraryCxts = [[AncillaryDataUtil, libEnv]],
             testAppCxts = [[test_AncillaryDataUtil, progEnv]],
             includes = listFiles(['AncillaryDataUtil/*.h']),
             data = listFiles(['data/*'],recursive=True))





