def ssr(pin,ton,tstop,q):
  from ssr_sw_class import ssr_sw
  q.put(1)
  ssr=ssr_sw(int(pin))
  ret=ssr.run(ton,tstop)
  q.put(0)
  return
