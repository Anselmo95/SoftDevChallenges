import gdb

class FindPointers (gdb.Command):
	"Find pointers given a starting address and a range"

	def __init__ (self):
		# https://www-zeuthen.desy.de/unix/unixguide/infohtml/gdb/Commands-In-Python.html
		super (FindPointers, self).__init__ ("fpointers", gdb.COMMAND_DATA, gdb.COMPLETE_COMMAND)

	def deref_address(self, add):
		addr = gdb.Value(add)
		type_pointer = gdb.lookup_type(addr.type.name).pointer()
		addr_pointer = addr.cast(type_pointer).dereference()
		type_pointer = gdb.lookup_type(addr_pointer.type.name).pointer()
		try:
			addr = addr_pointer.cast(type_pointer).dereference()
		except gdb.MemoryError:
			return -1

		return addr.address

	def invoke (self, arg, from_tty):
		argv = gdb.string_to_argv(arg)
		start_addr = int(argv[0],0)
		span = int(argv[1])
		end_addr = start_addr + span +1 

		for mem_add in range(start_addr,end_addr):
			#print('0x{0:x}'.format(mem_add))
			addr_pointed = self.deref_address(mem_add)
			#print('0x{0:x}'.format(mem_add), '-->', '0x{0:x}'.format(int(addr_pointed)))
			if start_addr <= int(addr_pointed) < end_addr:
				print ('Pointer at ' ,'0x{0:x}'.format(mem_add), '-->' ,addr_pointed)

FindPointers()