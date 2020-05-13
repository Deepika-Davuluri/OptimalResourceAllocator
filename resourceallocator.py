import collections

machine_capacities = {'Large': 10, 'XLarge': 20, '2XLarge': 40, '4XLarge': 80, '8XLarge': 160, '10XLarge': 320}
country_costs = {
    'New York': {'Large': 120, 'XLarge': 230, '2XLarge': 450, '4XLarge': 774, '8XLarge': 1400, '10XLarge': 2820},
    'India': {'Large': 140, 'XLarge': None, '2XLarge': 413, '4XLarge': 890, '8XLarge': 1300, '10XLarge': 2970},
    'China': {'Large': 110, 'XLarge': 200, '2XLarge': None, '4XLarge': 670, '8XLarge': 1180, '10XLarge': None}
}


class ResourceAllocator:
    def machineCapacitySum(self, candidates, target):
        candidates.sort()
        uber_list = self.find_machine_possibles(candidates, target)
        return uber_list

    def find_machine_possibles(self, candidates, target):
        uber_list = []

        if (target == 0):
            return [uber_list]

        if target is None:
            return None

        if (target < 0):
            return None

        i = 0
        for can in candidates:
            selec_candidates = candidates[i:len(candidates)]
            i += 1
            if (can > target):
                continue
            else:
                res = self.find_machine_possibles(selec_candidates, target - can)
            if (res is None):
                continue
            else:
                for r in res:
                    r.append(can)

                    new_dict = dict(collections.Counter(r))
                    counter_dict = {}
                    for key in new_dict.keys():
                        counter_dict[list(machine_capacities.keys())[list(machine_capacities.values()).index(key)]] = \
                            new_dict[key]

                    uber_list.append(r)

        if (len(uber_list) == 0):
            return None
        return uber_list

if __name__ == "__main__":
    resourceAllocator = ResourceAllocator()
    no_of_units = int(input("Enter the total number of units: "))
    no_of_hours = int(input("Enter the total number of hours: "))
    res = resourceAllocator.machineCapacitySum(list(machine_capacities.values()), no_of_units)

    min_costs_dict = {}
    min_items_dict = {}
    for country in country_costs.keys():
        min_costs_dict[country] = 999999999
        min_items_dict[country] = {}

    if res:
        for item in res:
            new_dict = dict(collections.Counter(item))
            counter_dict = {}
            for key in new_dict.keys():
                counter_dict[list(machine_capacities.keys())[list(machine_capacities.values()).index(key)]] = new_dict[key]

            for country in country_costs.keys():
                cost = 0
                for machine in counter_dict.keys():
                    if country_costs[country][machine]:
                        cost += country_costs[country][machine] * no_of_hours * counter_dict[machine]
                    else:
                        cost = 999999999

                if cost < min_costs_dict[country]:
                    min_costs_dict[country] = cost
                    min_items_dict[country] = counter_dict

        result = []
        for country in country_costs.keys():
            country_result = {}
            country_result['region'] = country
            country_result['total_cost'] = "$" + str(min_costs_dict[country])
            country_result['machines'] = [(k, v) for k, v in min_items_dict[country].items()]
            result.append(country_result)

        print({"Output": result})
    else:
        print("No Combinations found for the required Units")
