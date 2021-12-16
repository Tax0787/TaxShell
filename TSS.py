def ifs(bools, elses):
	strs = ''
	for i, j in bools.items():
		strs += 'if {}:\n{}\nel'.format(i, j)
	return strs + 'se:\n' + elses


class TaxShellClass:
	class CommandNotFoundError(Exception):
		pass

	def __init__(
	    self,
	    name,
	    mom,
	    split1,
	    split2,
	    ifs_bools,
	    ifs_elses,
	    sose='don\'t tuoch',
	):
		exec(
		    ifs(
		        {
		            'not type(split1) == str':
		            '    raise TypeError(\'the split1 is not string\')',
		            'not type(name) == str':
		            '    raise TypeError(\'the name is not string\')',
		            'not type(mom) == str':
		            '    raise TypeError(\'the mom is not string\')',
		            'not type(split2) == str':
		            '    raise TypeError(\'the split2 is not sting\')',
		            'not type(ifs_elses) == str':
		            '    raise TypeError(\'the ifs_else is not string\')',
		            'not type(ifs_bools) == dict':
		            '    raise TypeError(\'the ifs_bools is bot dictionary\')'
		        }, '    pass'))
		ifs_bools[
		    "Command == 'os'"] = '  Script += \'from os import system as s\\n  s(a[1])\''
		ifs_bools["Command == 'py'"] = '  Script += \'exec(a[1))\''
		ifs_bools[
		    "Command == 'git'"] = '  Script += \'from os import system as s\\n  s(\\\'git\\\' + a[1])\''
		ifs_bools["Command == 'exec'"] = '  Script += \'self.execution(a[1])\''
		ifs_bools[
		    "Command == 'comfile'"] = '  Script += \'self.comfile(a[1])\''
		ifs_bools["Command == 'shell'"] = '  Script += \'self.shell()\''
		ifs_bools["Command == ''"] = '  Script += \'\''
		self.split1 = split1
		self.name = name
		self.mom = mom
		self.split2 = split2
		self.ifs_elses = ifs_elses
		self.ifs_bools = ifs_bools
		sose = '''
class {}({}):
  def __init__(self, print_bool = False):
    if print_bool: print('ok')
  
  def execution(self, sose):
    Script = ''
    for i in sose.split(\'{}\'):
      a = i.split(\'{}\')
      Command = a[0]
      print(a)
      print(Command)
      print(Script)
      exec(ifs({}, \'\'\'{}\'\'\'))
      print(Script)
    print(Script)
    return Script
  
  def comfile(self, file):
    with open(file, 'r') as f:
      return self.execution(f.read())
  
  def shell(self):
    roop = True
    while roop:
      sose = input('>>> ') + '\\n'
      add = sose
      while not add == '':
        add = input('... ')
        sose += add + '\\n'
      print(self.execution(sose))'''.format(self.name, self.mom, self.split1,
		                                    self.split2, self.ifs_bools,
		                                    self.ifs_elses)
		self.sose = sose


a = TaxShellClass(
    'HiShellScript', '', '\\n', '>ω<',
    {'Command == \'hi\'': '  Script += \'print(\"hi\")\''}, '''
   raise CommandsNotFoundError(\'the command {} is not found\'.format(Command))'''
)
exec(a.sose)
a = HiShellScript()
a.shell()
