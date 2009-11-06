# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataUtil/SConscript,v 1.5 2009/08/26 19:51:03 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataUtil-01-00-04
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('AncillaryDataUtilLib', depsOnly = 1)
AncillaryDataUtil = libEnv.StaticLibrary('AncillaryDataUtil', listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataUtilLib')
test_AncillaryDataUtil = progEnv.Program('test_AncillaryDataUtil',['src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AncillaryDataUtil',
             libraryCxts = [[AncillaryDataUtil, libEnv]],
             testAppCxts = [[test_AncillaryDataUtil, progEnv]],
             includes = listFiles(['AncillaryDataUtil/*.h']),
             data = listFiles(['data/*'],recursive=True))





