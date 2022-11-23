from osgeo import gdal,ogr

def uni(shpPath, fname):
    """
    :param shpPath: 输入的矢量路径
    :param fname: 输出的矢量路径
    :return:
    """
    driver = ogr.GetDriverByName("ESRI Shapefile")
    dataSource = driver.Open(shpPath, 1)
    layer = dataSource.GetLayer()

    # 新建DataSource，Layer
    out_ds = driver.CreateDataSource(fname)
    out_lyr = out_ds.CreateLayer(fname, layer.GetSpatialRef(), ogr.wkbPolygon)
    def_feature = out_lyr.GetLayerDefn()
    # 遍历原始的Shapefile文件给每个Geometry做Buffer操作
    # current_union = layer[0].Clone()
    print('the length of layer:', len(layer))
    if len(layer) == 0:
        return

    for i, feature in enumerate(layer):
        geometry = feature.GetGeometryRef()
        if i == 0:
            current_union = geometry.Clone()
        current_union = current_union.Union(geometry).Clone()

        if i == len(layer) - 1:
            out_feature = ogr.Feature(def_feature)
            out_feature.SetGeometry(current_union)
            out_lyr.ResetReading()
            out_lyr.CreateFeature(out_feature)
