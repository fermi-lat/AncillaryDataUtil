# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataUtil/SConscript,v 1.2 2008/09/16 19:31:04 ecephas Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataUtil-01-00-03
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('AncillaryDataUtilLib', depsOnly = 1)
AncillaryDataUtil = libEnv.StaticLibrary('AncillaryDataUtil', listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataUtilLib')
test_AncillaryDataUtil = progEnv.Program('test_AncillaryDataUtil',['src/test/testMain.cxx'])

progEnv.Tool('registerObjects', package = 'AncillaryDataUtil',
             libraries = [AncillaryDataUtil],
             testApps = [test_AncillaryDataUtil],
             includes = listFiles(['AncillaryDataUtil/*.h']),
             data = listFiles(['data/*'],recursive=True))





