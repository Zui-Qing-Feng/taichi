import taichi as ti

def grad_test1():
  ti.cfg.use_llvm = True
  ti.set_gdb_trigger()

  x = ti.var(ti.i32)

  @ti.layout
  def place():
    ti.root.dense(ti.i, 1).place(x)

  ti.runtime.materialize()

  ti.runtime.prog = None
  ti.lang_core.test_throw()


grad_test1()
