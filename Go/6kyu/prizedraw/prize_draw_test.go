package prizedraw

import "testing"

func TestGetSomForSmallName(t *testing.T) {
	som := getSom("ab")
	if som != 5 {
		t.Errorf("GetSom returned an invalid value for a small name, got %d, expected %d", som, 5)
	}
}

func TestGetSomForMediumName(t *testing.T) {
	som := getSom("guidi")
	if som != 55 {
		t.Errorf("GetSom returned an invalid value for a medium name, got %d, expected %d", som, 55)
	}
}

func TestGetSomForBigName(t *testing.T) {
	som := getSom("apsejlnkw")
	if som != 120 {
		t.Errorf("GetSom returned an invalid value for a big name, got %d, expected %d", som, 120)
	}
}

func TestGetRankForFirstCapitalLetter(t *testing.T) {
	rank := getRank('A')
	if rank != 1 {
		t.Errorf("GetRank returned an invalid value for A, got %d, expected %d", rank, 1)
	}
}

func TestGetRankForFirstLowerLetter(t *testing.T) {
	rank := getRank('a')
	if rank != 1 {
		t.Errorf("GetRank returned an invalid value for a, got %d, expected %d", rank, 1)
	}
}
