def pixellayout(i, p, *rows): i["TrackTimingPixelPhase1/Layouts/" + p] = DQMItem(layout=rows)


### Digis
pixellayout(dqmitems, "01a - Timing_Digi_Barrel",
   [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}
      ] )

pixellayout(dqmitems, "01b - Timing_Digi_Forward",
   [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_digis_per_OnlineBlock_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}] )

### ADC
pixellayout(dqmitems, "02a - Timing_ADC_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_per_OnlineBlock_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "02b - Timing_ADC_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_per_OnlineBlock_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])

### NumCluster
pixellayout(dqmitems, "03a - Timing_Cluster_Number_Barrel",
   [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster value per lumisection in barrel",
      'draw': { 'withref': "no" }}] )
pixellayout(dqmitems, "03b - Timing_Cluster_Number_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/num_clusters_per_OnlineBlock_PXForward",
      'description': "Mean cluster value per lumisection in endcap",
      'draw': { 'withref': "no" }}])

### Cluster Charge
pixellayout(dqmitems, "04a - Timing_Cluster_Charge_Barrel",
  [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "04b - Timing_Cluster_Charge_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_per_OnlineBlock_PXForward",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "05a - Timing_size_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "05b - Timing_size_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Charge On track
pixellayout(dqmitems, "06a - Timing_charge_ontrack_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "06b - Timing_charge_ontrack_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Number of cluster on track
pixellayout(dqmitems, "07a - Timing_num_cluster_ontrack_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/num_clusters_ontrack_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "07b - Timing_num_cluster_ontrack_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/num_clusters_ontrack_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Residualx
pixellayout(dqmitems, "08a - Timing_residualx_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "08b - Timing_residualx_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Residualy
pixellayout(dqmitems, "09a - Timing_residualy_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_per_OnlineBlock_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "09b - Timing_residualy_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_per_OnlineBlock_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

############################## NON ONLINEBLOCK ##############################################

### ADC
pixellayout(dqmitems, "11a - Timing_ADC_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_PXBarrel",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "11b - Timing_ADC_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/adc_PXForward",
      'description': "Mean adc value per lumisection",
      'draw': { 'withref': "no" }}])
### Cluster Charge
pixellayout(dqmitems, "12a - Timing_Cluster_Charge_Barrel",
  [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_PXBarrel",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }} ] )
pixellayout(dqmitems, "12b - Timing_Cluster_Charge_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/charge_PXForward",
      'description': "Mean cluster charge per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Size
pixellayout(dqmitems, "13a - Timing_size_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "13b - Timing_size_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_MechanicalView/size_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Charge On track
pixellayout(dqmitems, "14a - Timing_charge_ontrack_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "14b - Timing_charge_ontrack_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/charge_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Residualx
pixellayout(dqmitems, "15a - Timing_residualx_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "15b - Timing_residualx_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_x_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )

### Residualy
pixellayout(dqmitems, "16a - Timing_residualy_Barrel",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_PXBarrel",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}])
pixellayout(dqmitems, "16b - Timing_residualy_Forward",
    [{ 'path': "TrackTimingPixelPhase1/Phase1_Track/residual_y_PXForward",
      'description': "Mean cluster size per lumisection in barrel",
      'draw': { 'withref': "no" }}] )
