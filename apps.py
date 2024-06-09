
from PIL import Image
import csv
import pickle
import math

with open(f"entro.en", "rb") as f:
  entro=pickle.load(f)
with open(f"questions.en", "rb") as f:
  quesk=pickle.load(f)
with open(f"attri.en", "rb") as f:
  attri=pickle.load(f)
with open("indics.indi", "rb") as f:
  indics=pickle.load(f)
with open("flexdata.csv", "r") as f:
  data={}
  c = csv.DictReader(f)
  salts=c.fieldnames[1:34]
  for salt in salts:
      data[salt]=[]
  for row in c:
    for salt in salts:
      data[salt].append(row[salt])

with open("flexdata.csv", "r") as f:
    R=csv.reader(f)
    data["total"]=[]
    for t in R:
      if t[1]!="NiCl2":
        lo=t[1:34]
        for i in range(len(lo)):
          lo[i]=int(lo[i])
        data["total"].append(sum(lo))

d={i: data[i] for i in data.keys() if i!="total"}

def probability(salt, evi):
  PE=[]
  for i in evi:
    if i[-1]!="'":
      PE.append((int(indics[i]), int(data[salt][indics[i]]), 0))
    else:
      PE.append((int(indics[i[0:-1]]), int(1-int(data[salt][indics[i[0:-1]]])), 1))
  e_s_=0
  for i in d.keys():
    if i!=salt:
      k=(1/33)
      for j in PE:
        if j[2]==1:
          attri=1-int(d[i][j[0]])
        else:
          attri=int(d[i][j[0]])
        k=k*attri
    if i!=salt:
      e_s_+=k
  e_s=1
  for i in PE:
    e_s=e_s*i[1]
  p=((1/33)*e_s)/((1/33)*e_s+e_s_+1e-15)
  return p

def entropy(mp):
  entropies=[]
  mostpro=mp
  m={}
  for i in mostpro:
    m=attri[i].union(m)
  m=list(m)
  for mk in m:
    l=entro[mk]
    for j in range(len(l)):
      l[j]=int(l[j])
    total_rows = 55
    p_1 = sum(l) / total_rows  # Proportion of 1's
    p_0 = 1 - p_1  # Proportion of 0's

    # Handle potential zero probabilities to avoid math domain error
    if p_1 == 0:
        p_1 = 1e-10  # Replace with a small non-zero value
    if p_0 == 0:
        p_0 = 1e-10
    overall_entropy = -(p_1 * math.log2(p_1) + p_0 * math.log2(p_0))
    entropies.append((mk, round(overall_entropy, 4)))
  entropies.sort(key=lambda x: x[1])
  g=[i[0] for i in entropies]
  g=g[-1: :-1]
  return g

import streamlit as st
st.title("Salt Akinator❤️")

st.caption("A Project by Sujal")

st.write('')


if 'mainqq' not in st.session_state:
   st.session_state.mainqq=None

if 'rad' not in st.session_state:
   st.session_state.rad=None

if 'q' not in st.session_state:
   st.session_state.q=1

if 'next' not in st.session_state:
   st.session_state.next=['color']

if 'r' not in st.session_state:
   st.session_state.r=[]

if 'lq' not in st.session_state:
   st.session_state.lq=None

if 'init' not in st.session_state:
   st.session_state.init=False

if 'state' not in st.session_state:
   st.session_state.state=True

def create_section():
    st.subheader(st.session_state.mainqq)
    st.caption(f'Qustion no. {st.session_state.q}')
    st.session_state.rad = st.radio('Select a option', ['Yes', 'No'], label_visibility='collapsed')
    row = st.columns(2)
    c = 0
    for i in row:
        if c == 0:
            con = i.container(border=False)
            con.button('Previous', key='button9')
        else:
            con = i.container(border=False)
            if con.button('Next'):
                mainp(st.session_state.rad)
                st.rerun()
        c += 1

def generate(proba=None):
  if proba!=None:
    st.session_state.next=entropy(proba)
  #ulta=["greencolor'", "nitst'", "niconfitst'", "bluecolor'", "blueflame'", "cutst'", "cuconfitst'", "yellowcolor'", "rredcolor'", "cotst'", "coconfitst'", "pinkcolor'", "mntst'", "mnconfitst'", "s2tst'", "s2confitst'", "as3tst'", "as3confitst'", "fe2tst'", "fe2confitst'", "ca2tst'", "bredflame'", "sr2confitst", "no2tst'", "no2confitst'", "groupii'", "po4tst'", "po4confitst'", "no3tst'", "no3confitst'", "zntst'", "znconfitst'", "fe3tst'", "fe3confitst'", "fe3confitst2'", "brtst'", "brconfitst'", "sr2tst", "redflame", "groupvi'", "mg2tst'", "mg2confitst'", "al3tst'", "al3confitst'", "groupv", "group'", "nh4tst'", "nh4confitst'", "groupiv'", "cltst'", "clconfitst'", "ch3cootst'", "ch3cooconfitst'", "co3tst", "co3confitst", "groupiii'", "groupi'", "pbtst'", "pbconfitst'", "pbconfitst2'", "so4tst'", "so4confitst'", "odour'", "color"]
  try:
    t=0
    while True:
      quesi=st.session_state.next[t]
      if quesi not in st.session_state.r and list(quesk[quesi][1])[0]!=st.session_state.lq:
        mainquestion=quesk[quesi][0]
        st.session_state.lq=list(quesk[quesi][1])[0]
        st.session_state.y=st.session_state.next[t]
        break
      else:
        t=t+1
  except:
    st.empty()
    st.session_state.state=None
  if proba==None and st.session_state.state==True:
    st.session_state.mainqq=mainquestion
    create_section()
    st.session_state.init=True
  if proba!=None st.session_state.state==True:
    st.session_state.mainqq=mainquestion
    return mainquestion

def mainp(k):
  if k=='Yes':
    st.session_state.r.append(st.session_state.y)
  else:
    st.session_state.r.append(st.session_state.y+"'")
  proba=[]
  for i in d.keys():
    p=round(100*probability(i, st.session_state.r))
    if p>0:
      proba.append(i)
      print('Probaility', i, p, '\b%')
    if p==100:
      st.session_state.state=False
      st.empty()
      st.session_state.salt=i
      break
  
  if st.session_state.state!=False:
    st.session_state.q+=1
    generate(proba)

if st.session_state.state==True:
  if st.session_state.init==False:
    generate()
  else:
    create_section()
else:
  if st.session_state.state==False:
    st.success(f'Your salt is {st.session_state.salt}')
  else:
    st.error('You have answered a question wrong!')
