def CTPPSTrackingStripLayout(i, p, *rows): i["CTPPS/TrackingStrip/Layouts/" + p] = DQMItem(layout=rows)
def CTPPSDiamondLayout(i,p, *rows): i["CTPPS/TimingDiamond/Layouts/" + p] = DQMItem(layout=rows)

#----- Totem strips
#

strips_stations = [ "sector 45/station 210", "sector 56/station 210" ]
strips_units = [ "nr", "fr" ]

# layouts with no overlays
for plot in [ "active planes", "activity in planes (2D)", "vfats with any problem", "track XY profile" ]:
  rows = list()
  for station in strips_stations:
    row = list()
    for unit in strips_units:
      row.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot)
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot, *rows)

# layouts with overlays
for plot in [ "active planes", "recognized patterns", "planes contributing to fit" ]:
  rows = list()
  for station in strips_stations:
    row = list()
    for unit in strips_units:
      hist_u = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " U"
      hist_v = "CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/"+plot + " V"
      row.append( { "path" : hist_u, "overlays" : [ hist_v ] } )
    rows.append(row)

  CTPPSTrackingStripLayout(dqmitems, plot + " UV", *rows)

#----- Diamond detectors
#

diamond_stations = [ "sector 45/station 220cyl/cyl_hr", "sector 56/station 220cyl/cyl_hr" ]

# layouts with no overlays
for plot in [ "active planes", "activity per FED BX", "hits in planes", "HPTDC Errors", "time over threshold", "" ]:
  rows = list()
  for station in diamond_stations:
    rows.append( "CTPPS/TimingDiamond/%{station}/%{plot}".format(station=station, plot=plot) )

  CTPPSDiamondLayout(dqmitems, plot, *rows)

#----- Summary plots
#

# per-BX plots
for suffix in [ "", " (short)" ]:
  plot_list = list()
  for station in strips_stations:
    for unit in strips_units:
      plot_list.append("CTPPS/TrackingStrip/"+station+"/"+unit+"_hr/activity per BX" + suffix)
  for station in diamond_stations:
    plot_list.append( "CTPPS/TimingDiamond/%{station}/activity per BX%{suffix}".format(station=station, suffix=suffix) )

  base_plot = "CTPPS/events per BX" + suffix
  CTPPSTrackingStripLayout(dqmitems, "activity per BX" + suffix, [ { "path" : base_plot, "overlays" : plot_list } ])

