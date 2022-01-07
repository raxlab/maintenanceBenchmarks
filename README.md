<!-- # maintenanceBenchmarks -->

# Benchmarks for Maintenance Problems


This repository has the supplemental materials for the article

*Improving prescriptive maintenance by incorporating post-prognostic information through chance constraints*

by [Anthony D. Cho](https://www.raxlab.science/author/anthony-d.-cho-lo/), [Rodrigo A. Carrasco](https://www.raxlab.science/members/rodrigo-a.-carrasco/), and [Gonzalo A. Ruz](https://gonzaloruz.com/index.html).

Paper information available here: [summary]().


## Files in this repository:

- **MachinesLocation.pdf**: Visualization of the Machines location in 2D space.

- **scenarioGenerator.py**: scenario maker script in python, sampling from a normal distribution for Remaining Useful Life (RUL).

- **datasets.xls**: contains some problem cases, each per sheet, which contains machine ID, component type ID, machine location (X, Y), Mean Time To Repair (MTTR), and RUL. A summary is provided in the following table.

	<center>

	| Sheet name      | Description                                                  |
	|-----------------|--------------------------------------------------------------|
	| Components_info | Component types with the Mean Time To Repair (MTTR) in hours |
	| Machine_info    | Machine types and their locations (X,Y)                      |
	| Problem_26      | 26 components (4 machines, 8 component types)                |
	| Problem_50      | 50 components (6 machines, 17 component types)               |
	| Problem_100     | 100 components (8 machines, 20 component types)              |
	| Problem_150     | 150 components (9 machines, 20 component types)              |
	| Problem_200     | 200 components (10 machines, 20 component types)             |
	| Problem_500     | 500 components (20 machines, 20 component types)             |
	| Problem_1000    | 1000 components (20 machines, 20 component types)            |

	</center>

---

