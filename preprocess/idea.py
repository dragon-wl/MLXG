# -*- coding: utf-8 -*-
# @Author:   Mi
# @Funciong:

'''

1）训练集

   按照一个一个mall来分开训练，还是全部一起训练；
   单独来数据可能会少 但是合在一起，那些wifi信息貌似定位到的经纬度也不一样

2）定位方法考虑

   a）wifi定位
     根据wifi信号强度以及相应的定位算法来定位，用户的行为信息辅助精确定位
     估计不行，wifi信号强度定位算法应该需要有一个基础地图（参考点？）

   b）机器学习
     将WiFi信息当做输入，经纬度作为输出，进行分类训练

3）如何算定位成功

   经纬度精度很高，每个商铺应该是一个范围，如何获得这个范围？

   经纬度作为输入还是输出？
   当做输入：输出mall_id 和 商铺_id
   当做输出：通过经纬度再次判断该经纬度在哪个商铺？


'''