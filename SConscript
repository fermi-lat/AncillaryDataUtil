# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataUtil/SConscript,v 1.9 2012/01/23 19:25:51 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataUtil-01-00-06
Import('baseEnv')
Import('listFiles')
Import('packages')
progEnv = baseEnv.Clone()
libEnv = baseEnv.Clone()

libEnv.Tool('addLinkDeps', package = 'AncillaryDataUtil', toBuild='static')
AncillaryDataUtil = libEnv.StaticLibrary('AncillaryDataUtil', listFiles(['src/*.cxx']))

progEnv.Tool('AncillaryDataUtilLib')
test_AncillaryDataUtil = progEnv.Program('test_AncillaryDataUtil',['src/test/testMain.cxx'])

progEnv.Tool('registerTargets', package = 'AncillaryDataUtil',
             staticLibraryCxts = [[AncillaryDataUtil, libEnv]],
             testAppCxts = [[test_AncillaryDataUtil, progEnv]],
             includes = listFiles(['AncillaryDataUtil/*.h']),
             data = listFiles(['data/*'],recursive=True))





