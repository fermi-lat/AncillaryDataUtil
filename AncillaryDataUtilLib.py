# $Header: /nfs/slac/g/glast/ground/cvs/GlastRelease-scons/AncillaryDataUtil/AncillaryDataUtilLib.py,v 1.1 2008/08/15 21:42:33 ecephas Exp $
def generate(env, **kw):
    if not kw.get('depsOnly', 0):
        env.Tool('addLibrary', library = ['AncillaryDataUtil'])
    env.Tool('facilitiesLib')
def exists(env):
    return 1;