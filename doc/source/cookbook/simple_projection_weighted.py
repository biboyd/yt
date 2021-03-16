import yt

# Load the dataset.
ds = yt.load("GalaxyClusterMerger/fiducial_1to3_b0.273d_hdf5_plt_cnt_0175")

# Create density-weighted projections of temperature (weighted line integrals)

yt.ProjectionPlot(
    ds, "x", ("gas", "temperature"), weight_field=("gas", "density")
).save()
yt.ProjectionPlot(
    ds, "y", ("gas", "temperature"), weight_field=("gas", "density")
).save()
yt.ProjectionPlot(
    ds, "z", ("gas", "temperature"), weight_field=("gas", "density")
).save()
