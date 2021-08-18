import CSV
using Plots

println("reading from file")
data = CSV.File("log.csv")

println("filtering bedroom_data")
bedroom_data = filter(data -> data[2] == "Bedroom", data)
livingr_data = filter(data -> data[2] == "Livingroom", data)

gr()
p = plot(map(data -> data[1], bedroom_data), map(data -> data[3], bedroom_data))
plot!(p, map(data -> data[1], livingr_data), map(data -> data[3], livingr_data))

savefig(p, "plot.pdf")
