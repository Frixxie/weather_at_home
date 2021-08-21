import CSV
import Plots

println("reading from log.csv")
data = CSV.File("log.csv")

println(data)

println("filtering bedroom_data")
bedroom_data = filter(data -> data[2] == "Bedroom", data)
println("filtering livingr_data")
livingr_data = filter(data -> data[2] == "Livingroom", data)

println("setting up backend")
Plots.gr()

println("Plotting")
p = Plots.plot(map(data -> data[1], bedroom_data), map(data -> data[3], bedroom_data))
Plots.plot!(p, map(data -> data[1], livingr_data), map(data -> data[3], livingr_data))

Plots.savefig(p, "plot.pdf")
