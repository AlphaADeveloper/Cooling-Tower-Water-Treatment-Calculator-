#city Water
City_Conductivity=1240
City_PH=8.45
City_Chlorides=450
City_Alkilinity=100
City_Hardness =8

#Tower1
Tower1_Conductivity=3200
Tower1_PH=9.00
Tower1_Chlorides=850
Tower1_Alkilinity=250
Tower1_Phos=8
Tower1_Hardness=20

#Closed loop1
Loop1_Conductivity=11.00
Loop1_PH=9.00
Loop1_Molybdate=22
Loop1_Nitrite=0
Loop1_Iron=1

#Tower2
Tower2_Conductivity=0
Tower2_PH=0
Tower2_Chlorides=0
Tower2_Alkilinity=0
Tower2_Phos=0
Tower2_Hardness=0

#Closed loop2
Loop2_Conductivity=0
Loop2_PH=0
Loop2_Nitrite=0
Loop2_Molybdate=0
Loop2_Iron=0

#Tower3
Tower3_Conductivity=0
Tower3_PH=0
Tower3_Chlorides=0
Tower3_Alkilinity=0
Tower3_Phos=0
Tower3_Hardness=0

#Closed loop3
Loop3_Conductivity=0
Loop3_PH=0
Loop3_Nitrite=0
Loop3_Molybdate=0
Loop3_Iron=0


#Tower4
Tower4_Conductivity=0
Tower4_PH=0
Tower4_Chlorides=0
Tower4_Alkilinity=0
Tower4_Phos=0
Tower4_Hardness=0

#Closed loop4
Loop4_Conductivity=0
Loop4_PH=0
Loop4_Nitrite=0
Loop4_Molybdate=0
Loop4_Iron=0

#END 

























#Tower Conductivity Cycles
Tower1_Conductivity_Cycles=Tower1_Conductivity/City_Conductivity
Tower2_Conductivity_Cycles=Tower2_Conductivity/City_Conductivity
Tower3_Conductivity_Cycles=Tower3_Conductivity/City_Conductivity
Tower4_Conductivity_Cycles=Tower4_Conductivity/City_Conductivity
#Tower Alkilinity Cycles
Tower1_Alkilinity_Cycles=Tower1_Alkilinity/City_Alkilinity
Tower2_Alkilinity_Cycles=Tower2_Alkilinity/City_Alkilinity
Tower3_Alkilinity_Cycles=Tower3_Alkilinity/City_Alkilinity
Tower4_Alkilinity_Cycles=Tower4_Alkilinity/City_Alkilinity
#Tower Chloride Cycles
Tower1_Chlorides_Cycles=Tower1_Chlorides/City_Chlorides
Tower2_Chlorides_Cycles=Tower2_Chlorides/City_Chlorides
Tower3_Chlorides_Cycles=Tower3_Chlorides/City_Chlorides
Tower4_Chlorides_Cycles=Tower4_Chlorides/City_Chlorides
#Tower Hardness Cycles
Tower1_Hardness_Cycles=Tower1_Hardness/City_Hardness
Tower2_Hardness_Cycles=Tower2_Hardness/City_Hardness
Tower3_Hardness_Cycles=Tower3_Hardness/City_Hardness
Tower4_Hardness_Cycles=Tower4_Hardness/City_Hardness

CAL=400/City_Alkilinity
Rec_Cycles= (CAL*City_Conductivity)
print("Recommended SetPoint:",Rec_Cycles )


Hardness_City=City_Hardness*17.1
Hardness_Tower1=Tower1_Hardness*17.1
Hardness_Tower2=Tower2_Hardness*17.1
Hardness_Tower3=Tower3_Hardness*17.1
Hardness_Tower4=Tower4_Hardness*17.1

#Closed Loop Calculation
#loop_one_iron=Loop1_Iron*8.5
#loop_two_iron=Loop2_Iron*8.5
#loop_three_iron=Loop3_Iron*8.5
#loop_four_iron=Loop4_Iron*8.5
loop_one_Molybdate=Loop1_Molybdate*8.5
loop_two_Molybdate=Loop2_Molybdate*8.5
loop_three_Molybdate=Loop3_Molybdate*8.5
loop_four_Molybdate=Loop4_Molybdate*8.5

#Closed Loop Nitrite Calculation




#City
if City_Conductivity>=0:
  print("City Conductivity:",City_Conductivity)
if  City_PH>=0:
  print("City PH:",City_PH)
if City_Chlorides>=0:
  print("City Chlorides:",City_Chlorides) 
if City_Alkilinity>=0:
  print("City Alkilinity:",City_Alkilinity)
if City_Hardness>=0:
  print("City Hardness:",Hardness_City )
  #Space
  print()
 #Tower1
if Tower1_Conductivity>=1:
  print("Tower One Conductivity:", Tower1_Conductivity)
if Tower1_PH>=1:
  print("Tower One PH:",Tower1_PH)
if Tower1_Chlorides>=1:
  print("Tower One Chlorides:",Tower1_Chlorides)
if Tower1_Alkilinity>=1:
  print("Tower One Alkilinity:",Tower1_Alkilinity)
if Tower1_Phos>=1:
  print("Tower One PHOS:", Tower1_Phos)
if Tower1_Hardness>=1:
  print("Tower One Hardness:", Hardness_Tower1 )
  #Space
print()
if Loop1_Conductivity>=1:
  print("Closed Loop One Conductivity:",Loop1_Conductivity) 
if Loop1_PH>=1:
  print("Closed Loop One Ph:",Loop1_PH)
if Loop1_Nitrite>=1:
  print("Closed Loop One Nitrite:",Loop1_Nitrite) 
if Loop1_Molybdate>=1:
  print("Closed loop one Molybdate:", loop_one_Molybdate)
if Loop1_Iron>=1:
  print("Closed Loop One Iron:", Loop1_Iron)
  
#space
  print()
  if Tower2_Conductivity>=1:
    print("Tower Two conductivity:", Tower2_Conductivity)
  if Tower2_PH>=1: 
    print("Tower Two PH: ",Tower2_PH )
  if Tower2_Chlorides>=1:
    print("Tower Two Chlorides:", Tower2_Chlorides)
  if Tower2_Alkilinity>=1:
    print("Tower Two Alkilinity:", Tower2_Alkilinity)
  if Tower2_Phos>=1:
    print("Towwer Two Phos:",Tower2_Phos)
  if Tower2_Hardness>=1:
    print("Tower Two Hardness:",Hardness_Tower2)
#Space
print()
 
if Loop2_Conductivity>=1:
  print("Closed Loop Two Conductivity:", Loop2_Conductivity)
if Loop2_PH>=1:
  print("Closed Loop Two PH:", Loop2_PH)
if Loop2_Nitrite>=1:
  print("Closed Loop Two Nitrite:", Loop2_Nitrite)
if Loop2_Molybdate>=1:
  print("Closed Loop Two Molybdate:", Loop2_Molybdate)
if Loop2_Iron>=1:
  print("Closed Loop Two Iron:",loop_two_iron)

#space
print()
if Tower3_Conductivity>=1:
  print("Tower Three Conductivity:", Tower3_Conductivity)
if Tower3_PH>=1:
  print("Tower Three PH:", Tower3_Conductivity)
if Tower3_Chlorides>=1:
  print("Tower Three Chlorides:",Tower3_Chlorides)
if Tower3_Alkilinity>=1:
  print("Tower Three Alkilinity:", Tower3_Alkilinity)
if Tower3_Phos>=1:
  print("Tower Three Phos:",Tower3_Phos)
if Tower3_Hardness>=1:
  print("Tower Three Hardness:", Hardness_Tower3)
#space
print()
if Loop3_Conductivity>=1:
 print("Closed Loop Three Conductivity:", Loop3_Conductivity)
if Loop3_PH>=1:
  print("Closed Loop Three PH:", Loop3_PH)
if Loop3_Nitrite>=1:
  print("Closed Loop Three Nitrite:", Loop3_Nitrite)
if Loop3_Molybdate>=1:
  print("Closed Loop Three Molybdate:", Loop3_Molybdate)
if Loop3_Iron>=1:
  print("Closed Loop Three Iron:", loop_three_iron)
#space
print()
if Tower4_Conductivity>=1:
  print("Tower Four Conductivity:", Tower4_Conductivity)
if Tower4_PH>=1:
  print("Tower Four PH:", Tower4_PH)
if Tower4_Chlorides>=1:
  print("Tower Four Chlorides:",Tower4_Chlorides)  
if Tower4_Alkilinity>=1:
  print("Tower Four Alkilinity:",Tower4_Alkilinity)
if Tower4_Phos>=1:
  print("Tower Four Phos:",Tower4_Phos)
if Tower4_Hardness>=1:
  print("Tower Four Hardness:",Hardness_Tower4)
#space
print()

if Loop4_Conductivity>=1:
  print("Closed Loop Four Conductivity:",Loop4_Conductivity)
if Loop4_Conductivity>=1:
  print("Closed Loop Four PH:",Loop4_PH)
if Loop4_Nitrite>=1:
  print("Closed Loop Four Nitrite:",Loop4_Nitrite)
if Loop4_Molybdate>=1:
  print("Closed Loop Four Molybdate:",Loop4_Molybdate)
if Loop4_Iron>=1:
  print("Closed Loop Four Iron:",loop_four_iron)

#space
print()

print(" Conductivity Cycles:")


print("Tower One Conductivity Cycles:[",Tower1_Conductivity_Cycles,"]") 
print("Tower Two Conductivity Cycles:[",Tower2_Conductivity_Cycles,"]")
print("Tower Three Conductivity Cycles:[",Tower3_Conductivity_Cycles,"]")
print("Tower Four Conductivity Cycles:[",Tower4_Conductivity_Cycles,"]")  
#Space
print()
#Alkilinity Cycles
print("Alkilinity Cycles:")
print("Tower One Alkilinity Cycles:[", Tower1_Alkilinity_Cycles,"]")
print("Tower Two Alkilinity Cycles:[", Tower2_Alkilinity_Cycles,"]")
print("Tower Three Alkilinity Cycles:[",Tower3_Alkilinity_Cycles,"]")
print("Tower Four Alkilinity Cycles:[", Tower4_Alkilinity_Cycles,"]")
#Space 
print()
#Chloride Cycles

print("Tower Chloride Cycles:")
print("Tower One Chloride Cycles:[",Tower1_Chlorides_Cycles,"]")
print("Tower Two Chloride Cycles:[",Tower2_Chlorides_Cycles,"]")
print("Tower Three Chloride Cycles:[",Tower3_Chlorides_Cycles,"]")
print("Tower Four Chloride Cycles:[", Tower4_Chlorides_Cycles,"]")
#Space
print()
# Hardness Cycles

print("Towers Hardness Cycles:")
print("Tower One Hardness Cycles:[", Tower1_Hardness_Cycles,"]")
print("Tower Two Hardness Cycles:[", Tower2_Hardness_Cycles,"]")
print("Tower Three Hardness Cycles:[",Tower3_Hardness_Cycles,"]")
print("Tower Four Hardness Cycles:[",Tower4_Hardness_Cycles,"]")

