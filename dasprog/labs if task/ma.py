def traffic_light(M, N, T):
    # Durasi siklus lampu lalu lintas
    red_duration = 20
    yellow_duration = 5
    green_duration = 60
    cycle_duration = red_duration + yellow_duration + green_duration
    
    # Jumlah mobil yang dapat melewati lampu hijau dalam satu siklus
    cars_passed_per_cycle = green_duration // 5
    
    # Hitung jumlah siklus penuh dalam waktu T
    full_cycles = T // cycle_duration
    remaining_time = T % cycle_duration
    
    # Hitung total mobil yang dapat melewati lampu dalam waktu T
    total_passed_cars = full_cycles * cars_passed_per_cycle
    if remaining_time > red_duration + yellow_duration:
        remaining_green_time = remaining_time - (red_duration + yellow_duration)
        total_passed_cars += remaining_green_time // 5
    
    # Hitung jumlah mobil yang tersisa di jalan
    total_cars = M + N
    remaining_cars = max(total_cars - total_passed_cars, 0)
    
    # Tentukan apakah Anda bisa melewati lampu
    if total_passed_cars >= M:
        print("YES!", remaining_cars)
    else:
        print("NO!", remaining_cars)

# Input
M, N, T = map(int, input().split())
traffic_light(M, N, T)
