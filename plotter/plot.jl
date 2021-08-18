import CSV
using Plots

data = CSV.File("log.csv")

bedroom_data = filter(data -> data[2] == "Bedroom", data)

dt = map(data -> data[1], bedroom_data)
temp = map(data -> data[3], bedroom_data)

gr()
p = plot(dt, temp)

savefig(p, "test.pdf")
