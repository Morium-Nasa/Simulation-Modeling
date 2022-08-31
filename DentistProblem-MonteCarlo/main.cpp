#include <bits/stdc++.h>

using namespace std;

struct Category
{
    string type;
    int time_required;
    int number_of_patients;
    float probability;
    float cumilitive_probability;
    int random_number;
};

struct Time
{
    int hour;
    int minute;

    int ellapsed_minute() {
        return hour*60 + minute;
    }
};


struct Simulation
{
    int patient;
    Time arrival_time;
    int random_number;
    Category category;
    int servce_time_needed;
    Time service_start_time;
    Time service_end_time;
    int waiting_time;
    int idle_time;
};


Category get_category_by_random_number(Category categories[],int category_size, int random_number)
{
    for(int i=0; i< category_size; i++) {
        if(random_number <= categories[i].random_number ) {
            return categories[i];
        }
    }
    // return first item for now
    return categories[0];
}

Time add_minutes_to_time(Time t, int minutes)
{
    t.minute += minutes;
     if(t.minute >= 60) {
        t.hour += t.minute / 60;
        t.minute = t.minute % 60;
    }
    return t;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    int n;
    printf("Enter total number of categories: ");
    cin >> n;
    cout << "Enter " << n << " category informations: " << endl;
    Category categories[n];
    int total_patients = 0;
    for(int i=0; i<n; i++) {
        cout << "Category " << (i+1) << " type: ";
        cin >> categories[i].type;
        cout << "Time Required (in minutes): ";
        cin >> categories[i].time_required;
        cout << "No. of patients: ";
        cin >> categories[i].number_of_patients;

        total_patients += categories[i].number_of_patients;
    }

    // calculate probability
    for(int i=0; i<n; i++) {
        categories[i].probability = (float) categories[i].number_of_patients / (float) total_patients;

        if(i == 0) categories[i].cumilitive_probability = categories[i].probability;
        else categories[i].cumilitive_probability = categories[i-1].cumilitive_probability + categories[i].probability;

        categories[i].random_number = ((int) (categories[i].cumilitive_probability * 100 )) - 1;
    }

    // print table 1
    cout << "\n======== TABLE 1 ===========" << endl;
    cout << "Type, " << "Probabiltiy, " << "C. Probability, " << "Random Number" << endl;
    for(int i=0; i<n ;i++) {
        cout << categories[i].type << ", " << categories[i].probability << ", " << categories[i].cumilitive_probability << ", " << ((i==0) ? 0 : (categories[i-1].random_number+1)) << " - " << categories[i].random_number << endl;
    }
    cout << "==============================" << endl;
    cout << endl;



    cout << "Total simulation times in minute: ";
    int toal_simulation_time;
    cin >> toal_simulation_time;
    cout << "Average service time per patient: ";
    int avg_service_time;
    cin >> avg_service_time;

    int total_simulation = toal_simulation_time / avg_service_time;

    Time start_time;
    cout << "Enter starting time in hh:mm format: (i.e. 08:00) ";
    scanf("%2d:%2d", &start_time.hour, &start_time.minute);


    int random_numbers[total_simulation + 1];

    cout << "Enter " << total_simulation << " random numbers: ";

    for(int i=0; i<total_simulation; i++) {
        cin >> random_numbers[i];
    }

    int total_waiting_time = 0;
    int total_idle_time = 0;

    // run the simulation
    Simulation simulations[total_simulation];

    Time arrival_time = start_time;
    for(int i=0; i<total_simulation; i++) {
        simulations[i].patient = i+1;
        simulations[i].random_number = random_numbers[i];
        simulations[i].category = get_category_by_random_number(categories, n, random_numbers[i]);
        simulations[i].servce_time_needed = simulations[i].category.time_required;

        if(i>0) {
            arrival_time = add_minutes_to_time(arrival_time, avg_service_time);
        }

        simulations[i].arrival_time = arrival_time;

        if(i==0) {
            simulations[i].service_start_time = arrival_time;
            simulations[i].service_end_time = add_minutes_to_time(arrival_time, simulations[i].servce_time_needed);

            simulations[i].waiting_time = 0;
            simulations[i].idle_time = 0;

        } else {

            simulations[i].service_start_time = simulations[i].arrival_time.ellapsed_minute() > simulations[i-1].service_end_time.ellapsed_minute() ?
                    simulations[i].arrival_time : simulations[i-1].service_end_time;
            simulations[i].service_end_time = add_minutes_to_time(simulations[i].service_start_time, simulations[i].servce_time_needed);

            if(simulations[i].service_start_time.ellapsed_minute() > simulations[i].arrival_time.ellapsed_minute()) {
                simulations[i].waiting_time = simulations[i].service_start_time.ellapsed_minute() - simulations[i].arrival_time.ellapsed_minute();
            }
            else {
                simulations[i].waiting_time = 0;
            }

            if(simulations[i].arrival_time.ellapsed_minute() > simulations[i-1].service_end_time.ellapsed_minute()) {
                simulations[i].idle_time = simulations[i].arrival_time.ellapsed_minute() - simulations[i-1].service_end_time.ellapsed_minute();
            } else {
                simulations[i].idle_time = 0;
            }
        }

        total_waiting_time += simulations[i].waiting_time;
        total_idle_time += simulations[i].idle_time;


    }

     // print table 2
    cout << "\n======== TABLE 2 ===========" << endl;
    cout << "Patient, " << "Scheduled Arrival, " << "Random Number, " << "Category, " << "Service Time Needed" << endl;
    for(int i=0; i<total_simulation ;i++) {
        cout << simulations[i].patient << ", " ;
        printf("%02d:%02d, ", simulations[i].arrival_time.hour , simulations[i].arrival_time.minute);
        cout << simulations[i].random_number << ", " << simulations[i].category.type << ", " << simulations[i].servce_time_needed << endl;
    }
    cout << "==============================" << endl;
    cout << endl;


      // print table 2
    cout << "\n======== FINAL TABLE ===========" << endl;
    cout << "Patient, " << "Arrival, " << "Service Start, " << "Service Duration, " <<  "Service Ends, " << "Waiting in mins, " <<  "Idle Time" << endl;
    for(int i=0; i<total_simulation ;i++) {
        cout << simulations[i].patient << ", " ;
        printf("%02d:%02d, ", simulations[i].arrival_time.hour , simulations[i].arrival_time.minute);
        printf("%02d:%02d, ", simulations[i].service_start_time.hour , simulations[i].service_start_time.minute);
        cout << simulations[i].servce_time_needed << ", ";
        printf("%02d:%02d, ", simulations[i].service_end_time.hour , simulations[i].service_end_time.minute);
        cout << simulations[i].waiting_time << ", " << simulations[i].idle_time << endl;
    }
    cout << "==============================" << endl;
    cout << endl;


    float avg_waiting_time = (float) total_waiting_time / (float) total_simulation;
    float avg_idle_time = (float) total_idle_time / (float) total_simulation;

    cout << "Average Waiting Time " << avg_waiting_time << endl;
    cout << "Average Idle Time " << avg_idle_time << endl;



    return 0;
}
