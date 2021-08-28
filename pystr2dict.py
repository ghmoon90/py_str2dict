def dict2file( src, szfile ):
  with open(szfile,mode='wb') as f:
    f.write( str(src).encode('utf-8'))

def file2dict(szfile):
  with open(szfile,mode='r') as f:
    exec( 'temp_dict=' + f.read())
  return temp_dict
