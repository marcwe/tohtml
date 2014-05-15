#!/usr/bin/python



f = open('workfile1', 'w')

myList=['GEO_8245.JPG', 'GEO_8246.JPG', 'GEO_8248.JPG', 'GEO_8249.JPG',
'GEO_8252.JPG', 'GEO_8254.jpg', 'GEO_8274.jpg', 'GEO_8286.jpg', 'GEO_8287.JPG',
'GEO_8307.JPG', 'GEO_8313.JPG', 'GEO_8318.JPG', 'GEO_8319.JPG', 'GEO_8320.JPG',
'GEO_8324.JPG', 'GEO_8327.JPG', 'GEO_8330.JPG', 'GEO_8449.JPG', 'GEO_8456.JPG',
'GEO_8472_1.JPG', 'GEO_8472.JPG', 'GEO_8483.JPG', 'GEO_8489.JPG',
'PCO_1511.JPG', 'PCO_1512.JPG', 'PCO_1513.JPG', 'PCO_1514.JPG', 'PCO_1515.JPG',
'PCO_1516.JPG', 'PCO_1518.jpg', 'PCO_1519.jpg', 'PCO_1520.jpg', 'PCO_1521.jpg',
'PCO_1522.jpg', 'PCO_1523.jpg', 'PCO_1524.jpg', 'PCO_1525.jpg', 'PCO_1526.jpg',
'PCO_1527.jpg', 'PCO_1529.jpg', 'PCO_1530.jpg', 'PCO_1531.jpg', 'PCO_1532.jpg',
'PCO_1533.jpg', 'PCO_1534.jpg', 'PCO_1536.jpg', 'PCO_1537.jpg', 'PCO_1538.jpg',
'PCO_1539.jpg', 'PCO_1540.jpg', 'PCO_1541.jpg', 'PCO_1542.jpg', 'PCO_1543.jpg',
'PCO_1544.jpg', 'PCO_1546.jpg', 'PCO_1547.jpg', 'PCO_1548.jpg', 'PCO_1549.jpg',
'PCO_1550.jpg', 'PCO_1551.jpg', 'PCO_1552.jpg', 'PCO_1553.jpg', 'PCO_1554.jpg',
'PCO_1560.jpg', 'PCO_1561.jpg', 'PCO_1563.jpg', 'PCO_1564.jpg', 'PCO_1565.jpg',
'PCO_1566.jpg', 'PCO_1569.jpg', 'PCO_1570.jpg', 'PCO_1571.jpg', 'PCO_1572.jpg',
'PCO_1573.jpg', 'PCO_1574.jpg', 'PCO_1575.jpg', 'PCO_1576.jpg', 'PCO_1577.jpg',
'PCO_1578.jpg', 'PCO_1579.jpg', 'PCO_1580.jpg', 'PCO_1581.jpg', 'PCO_1582.jpg',
'PCO_1584.jpg', 'PCO_1585.jpg', 'PCO_1586.jpg', 'PCO_1587.jpg', 'PCO_1588.jpg',
'PCO_1589.jpg', 'PCO_1590.jpg', 'PCO_1591.jpg', 'PCO_1592.jpg', 'PCO_1593.jpg',
'PCO_1594.jpg', 'PCO_1595.jpg', 'PCO_1596.jpg', 'PCO_1597.jpg', 'PCO_1598.jpg',
'PCO_1599.jpg', 'PCO_1600.jpg', 'PCO_1601.jpg', 'PCO_1602.jpg', 'PCO_1603.jpg',
'PCO_1604.jpg', 'PCO_1605.jpg', 'PCO_1607.jpg', 'PCO_1608.jpg', 'PCO_1609.jpg',
'PCO_1610.jpg', 'PCO_1611.jpg', 'PCO_1612.jpg', 'PCO_1614.jpg', 'PCO_1616.jpg',
'PCO_1618.jpg', 'PCO_1619.jpg', 'PCO_1620.jpg', 'PCO_1621.jpg', 'PCO_1622.jpg',
'PCO_1623.jpg', 'PCO_1624.jpg', 'PCO_1626.jpg', 'PCO_1627.jpg', 'PCO_1628.jpg',
'PCO_1629.jpg', 'PCO_1630.jpg', 'PCO_1631.jpg', 'PCO_1632.jpg', 'PCO_1633.jpg',
'PCO_1634.jpg', 'PCO_1635.jpg', 'PCO_1636.jpg', 'PCO_1637.jpg', 'PCO_1638.jpg',
'PCO_1639.jpg', 'PCO_1640.jpg', 'PCO_1641.jpg', 'PCO_1642.jpg', 'PCO_1643.jpg',
'PCO_1644.jpg', 'PCO_1645.jpg', 'PCO_1646.jpg', 'PCO_1648.jpg', 'PCO_1649.jpg',
'PCO_1650.jpg', 'PCO_1651.jpg', 'PCO_1652.jpg', 'PCO_1653.jpg', 'PCO_1654.jpg',
'PCO_1655.jpg', 'PCO_1656.jpg', 'PCO_1657.jpg', 'PCO_1658.jpg', 'PCO_1659.jpg',
'PCO_1660.jpg', 'PCO_1661.jpg', 'PCO_1662.jpg', 'PCO_1663.jpg', 'PCO_1664.jpg',
'PCO_1666.jpg', 'PCO_1667.jpg', 'PCO_1668.jpg', 'PCO_1669.jpg', 'PCO_1671.jpg',
'PCO_1672.jpg', 'PCO_1674.jpg', 'PCO_1675.jpg', 'PCO_1676.jpg', 'PCO_1677.jpg',
'PCO_1678.jpg', 'PCO_1680.jpg', 'PCO_1681.jpg', 'PCO_1682.jpg', 'PCO_1683.jpg',
'PCO_1684.jpg', 'PCO_1685.jpg', 'PCO_1688.jpg', 'PCO_1689.jpg', 'PCO_1690.jpg',
'PCO_1691.jpg', 'PCO_1692.jpg', 'PCO_1693.jpg', 'PCO_1694.jpg', 'PCO_1695.jpg',
'PCO_1696.jpg', 'PCO_1698.jpg', 'PCO_1699.jpg', 'PCO_1700.jpg', 'PCO_1701.jpg',
'PCO_1702.jpg', 'PCO_1703.jpg', 'PCO_1704.jpg', 'PCO_1705.jpg', 'PCO_1706.jpg',
'PCO_1707.jpg', 'PCO_1709.jpg', 'PCO_1710.jpg', 'PCO_1711.jpg', 'PCO_1712.jpg',
'PCO_1713.jpg', 'PCO_1714.jpg', 'PCO_1715.jpg', 'PCO_1716.jpg', 'PCO_1717.jpg',
'PCO_1718.jpg', 'PCO_1720.jpg', 'PCO_1722.jpg', 'PCO_1723.jpg', 'PCO_1724.jpg',
'PCO_1725.jpg', 'PCO_1726.jpg', 'PCO_1727.jpg', 'PCO_1728.jpg', 'PCO_1729.jpg',
'PCO_1730.jpg', 'PCO_1731.jpg', 'PCO_1732.jpg', 'PCO_1733.jpg', 'PCO_1734.jpg',
'PCO_1735.jpg', 'PCO_1736.jpg', 'PCO_1737.jpg', 'PCO_1738.jpg', 'PCO_1739.jpg',
'PCO_1740.jpg', 'PCO_1741.jpg', 'PCO_1742.jpg', 'PCO_1744.jpg', 'PCO_1745.jpg',
'PCO_1746.jpg', 'PCO_1748.jpg', 'PCO_1749.jpg', 'PCO_1750.jpg', 'PCO_1751.jpg',
'PCO_1755.jpg', 'PCO_1756.jpg', 'PCO_1757.jpg', 'PCO_1758.jpg', 'PCO_1759.jpg',
'PCO_1760.jpg', 'PCO_1761.jpg', 'PCO_1763.jpg', 'PCO_1764.jpg', 'PCO_1765.jpg',
'PCO_1766.jpg', 'PCO_1767.jpg', 'PCO_1769.jpg', 'PCO_1771.jpg', 'PCO_1772.jpg',
'PCO_1774.jpg', 'PCO_1775.jpg', 'PCO_1777.jpg', 'PCO_1779.jpg', 'PCO_1780.jpg',
'PCO_1782.jpg', 'PCO_1783.jpg', 'PCO_1784.jpg', 'PCO_1787.jpg', 'PCO_1789.jpg']



i = 0
while i < len(myList):

	print myList[i]

	fil = myList[i]

	f.write ('<td><a href="full/')
	f.write (fil)
	f.write ('"><img src="')
	f.write (fil)
	f.write ('" alt="')
	f.write (fil)
	f.write ('" /></a></td>')
	f.write ('\n')
 
	if (i+1)%5==0: f.write ('</tr><tr>\n')
	i = i + 1
f.closed