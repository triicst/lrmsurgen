from distutils.core import setup

import time

gmt = time.gmtime()
version = 'git-%04d%02d%02d' % (gmt.tm_year, gmt.tm_mon, gmt.tm_mday)

setup(name='lrmsurgen',
      version=version,
      description='LRMS UR Generator',
      author='Henrik Thostrup Jensen',
      author_email='htj@ndgf.org',
      url='http://www.ndgf.org/',
      packages=['lrmsurgen'],
      scripts = ['lrms-ur-generator', 'lrms-ur-registrant']
)

