package com.example.cvc_thedons;

import androidx.annotation.RequiresApi;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.concurrent.ThreadLocalRandom;

import static android.widget.Toast.*;

public class MainActivity3 extends AppCompatActivity {

    @RequiresApi(api = Build.VERSION_CODES.LOLLIPOP)
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main3);
        ListView listView = (ListView) findViewById(R.id.serviceList);

        ArrayList<String> arrayList = new ArrayList<>();
        int pret = getIntent().getExtras().getInt("Cost");
        int index = ThreadLocalRandom.current().nextInt(0, 5);
        ArrayList<String> luxury = new ArrayList<>();
        luxury.add("Auto Excel");
        luxury.add("Elite Auto Repair");
        luxury.add("Five Star Frame");
        luxury.add("King Mechanic");
        luxury.add("Perfection Auto Repair");
        ArrayList<String> premium = new ArrayList<>();
        premium.add("A+ Auto Care");
        premium.add("Car Doctor");
        premium.add("F.A.S.T Auto Repair");
        premium.add("Longlife Automotive");
        premium.add("Superformance");
        ArrayList<String> medium = new ArrayList<>();
        medium.add("The Carbon Hood");
        medium.add("Wish Motors");
        medium.add("Fine Crew");
        medium.add("Ocean Auto");
        medium.add("RC Automotive");
        ArrayList<String> economic = new ArrayList<>();
        economic.add("The Car Guys");
        economic.add("Auto Excel");
        economic.add("Auto Nation");
        economic.add("Little Red Wagon");
        economic.add("Rolling Right");
        ArrayList<String> lowcost = new ArrayList<>();
        lowcost.add("Discount Auto");
        lowcost.add("One Solution Auto");
        lowcost.add("Time Wheel");
        lowcost.add("The Auto Man");
        lowcost.add("Mr. Fix-It-All");

        String luxuryService = luxury.get(index) + '\n' + "Price: " + String.valueOf(1.75*pret) + " usd" + '\n' + "Distance: " + String.valueOf((int)((index+1))) +  " km" + '\n' + "Repair time: "  + String.valueOf((int)(index+2))+ " days";
        String premiumService = premium.get(index) + '\n' + "Price: " + String.valueOf(1.5*pret) + " usd" + '\n' + "Distance: " + String.valueOf((int)((index+1) * 1.5)) +  " km" +  '\n' + "Repair time: " + String.valueOf((int)(1.5*(index+2)))+ " days";
        String mediumService = medium.get(index) + '\n' + "Price: " + String.valueOf(pret) + " usd" + '\n' + "Distance: " + String.valueOf((int)((index+1) * 1.75)) +  " km" +  '\n' + "Repair time: " + String.valueOf((int)(2*(index+2)))+ "days";
        String economicService = economic.get(index) + '\n' + "Price: " + String.valueOf(0.75*pret) + " usd" + '\n' + "Distance: " + String.valueOf((int)((index+1) * 2)) +  " km" +  '\n' + "Repair time: " + String.valueOf((int)(2.5*(index+2)))+ " days";
        String lowcostService = lowcost.get(index) + '\n' + "Price: " + String.valueOf(0.5*pret) + " usd" + '\n' + "Distance: " + String.valueOf((int)((index+1) * 2.5)) +  " km" +  '\n' + "Repair time: " + String.valueOf((int)(3*(index+2))) + " days";
        arrayList.add(luxuryService);
        arrayList.add(premiumService);
        arrayList.add(mediumService);
        arrayList.add(economicService);
        arrayList.add(lowcostService);


        ArrayAdapter arrayAdapter = new ArrayAdapter(this, R.layout.mytextview, arrayList);
        listView.setAdapter(arrayAdapter);

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView<?> adapterView, View view, int position, long id) {
                String namesv = "";
                if(position == 0)
                    namesv = luxury.get(index);
                if(position == 1)
                    namesv = premium.get(index);
                if(position == 2)
                    namesv = medium.get(index);
                if(position == 3)
                    namesv = economic.get(index);
                if(position == 4)
                    namesv = lowcost.get(index);
                Toast.makeText(getApplicationContext(), "Apointment booked:" + namesv, LENGTH_LONG).show();
            }
        });
    }
}