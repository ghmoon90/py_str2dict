#%%
def dict2file( src, szfile ):
  with open(szfile,mode='wb') as f:
    f.write( str(src).encode('utf-8'))

def file2dict(szfile):

  with open(szfile,mode='r') as f:
    cmd = 'temp_dict=' + f.read()

  exec( cmd )

  return  locals()['temp_dict']
