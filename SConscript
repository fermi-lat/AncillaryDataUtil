# -*- python -*-
# $Header: /nfs/slac/g/glast/ground/cvs/AncillaryDataUtil/SConscript,v 1.10 2012/08/18 01:22:28 jrb Exp $
# Authors: N.Omodei <nicola.omodei@pi.infn.it>
# Version: AncillaryDataUtil-01-01-00
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





