<?xml version="1.0" encoding="UTF-8"?>
<tileset version="1.10" tiledversion="1.11.0" name="Fences" tilewidth="108" tileheight="86" tilecount="10" columns="0">
 <grid orientation="orthogonal" width="1" height="1"/>
 <tile id="0">
  <image source="../objects/fence_5.png" width="103" height="33"/>
 </tile>
 <tile id="1">
  <image source="../objects/bfence_1.png" width="76" height="24"/>
 </tile>
 <tile id="2">
  <image source="../objects/bfence_2.png" width="12" height="23"/>
 </tile>
 <tile id="3">
  <image source="../objects/bfence_3.png" width="78" height="86"/>
 </tile>
 <tile id="4">
  <image source="../objects/bfence_4.png" width="31" height="86"/>
 </tile>
 <tile id="5">
  <image source="../objects/bfence_5.png" width="108" height="32"/>
 </tile>
 <tile id="6">
  <image source="../objects/fence_1.png" width="70" height="18"/>
 </tile>
 <tile id="7">
  <image source="../objects/fence_2.png" width="6" height="18"/>
 </tile>
 <tile id="8">
  <image source="../objects/fence_3.png" width="70" height="81"/>
 </tile>
 <tile id="9">
  <image source="../objects/fence_4.png" width="30" height="82"/>
 </tile>
 <wangsets>
  <wangset name="Conjunto Sem Nome" type="edge" tile="-1">
   <wangcolor name="Cerca-madeira" color="#ff0000" tile="-1" probability="1"/>
   <wangcolor name="Cerca-pedra" color="#00ff00" tile="-1" probability="1"/>
   <wangtile tileid="1" wangid="0,0,2,0,0,0,2,0"/>
   <wangtile tileid="4" wangid="2,0,0,0,2,0,0,0"/>
   <wangtile tileid="6" wangid="0,0,1,0,0,0,1,0"/>
   <wangtile tileid="9" wangid="1,0,0,0,1,0,0,0"/>
  </wangset>
 </wangsets>
</tileset>
