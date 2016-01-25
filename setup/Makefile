CXX=g++
CXXFLAGS=-std=c++11 -Wall -Wshadow

%: %.cpp
	$(CXX) $^ -o $@ -O2 $(CXXFLAGS)

%_g: %.cpp
	$(CXX) $^ -o $@ -g $(CXXFLAGS)

