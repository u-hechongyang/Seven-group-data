from pyquery import PyQuery as pq

html='''
<div class="base">
<div class="name">基本属性</div>
<div class="content">
  <ul>
        <li><span class="label">房屋户型</span>3室2厅1厨1卫</li>
        <li><span class="label">所在楼层</span>中楼层 (共6层)</li>
        <li><span class="label">建筑面积</span>89.48㎡</li>
        <li><span class="label">户型结构</span>平层</li>
        <li><span class="label">套内面积</span>77.72㎡</li>
        <li><span class="label">建筑类型</span>板塔结合</li>
        <li><span class="label">房屋朝向</span>南 北</li>
        <li><span class="label">建筑结构</span>钢混结构</li>
        <li><span class="label">装修情况</span>精装</li>
        <li><span class="label">梯户比例</span>一梯两户</li>
        <li><span class="label">配备电梯</span>无</li>
        <li><span class="label">产权年限</span>70年</li>
  </ul>
</div>
</div>
'''

doc = pq(html)
list_content = list()
lis = doc('.base .content li')
for li in lis.items():
    #['3室2厅1厨1卫', '中楼层 (共6层)', '89.48㎡', '平层', '77.72㎡', '板塔结合', '南 北', '钢混结构', '精装', '一梯两户', '无', '70年']
    #print(li.children().text()) 提取span中的内容
    li.find('span').remove()
    list_content.append(li.text())
print(list_content)

houses = list_content[0]
rooms = int(houses[0:houses.index("室")])
halls = int(houses[houses.index("室")+1:houses.index("厅")])
floors = list_content[1]
floors = floors[:floors.index("层")]
house_struct = list_content[3]
floor_area = list_content[4]
floor_area = float(floor_area[0:floor_area.index("㎡")])
directions = list_content[6]
decoration = list_content[8]
elevator_porporation = list_content[9]
iselevator = list_content[10]
property_year = list_content[11]
property_year = int(property_year[0:property_year.index("年")])

print(rooms," ",halls," ",floors," ",house_struct," ",floor_area," ",directions," ",decoration," ",elevator_porporation," ",iselevator," ",property_year," ")


