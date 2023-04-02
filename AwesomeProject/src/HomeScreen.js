import React, { useState } from 'react';
import { View, StyleSheet } from 'react-native';
import { Input, Button } from 'react-native-elements';
import axios from 'axios';

const HomeScreen = () => {
  const [searchQuery, setSearchQuery] = useState('');
  const [colleges, setColleges] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await axios.get(`https://api.example.com/colleges?q=${searchQuery}`);
      setColleges(response.data);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <Input
        placeholder="Enter a college name or location"
        value={searchQuery}
        onChangeText={setSearchQuery}
      />
      <Button
        title="Search"
        onPress={handleSearch}
      />
      {colleges.map((college) => (
        <View key={college.id}>
          <Text>{college.name}</Text>
          <Text>{college.location}</Text>
        </View>
      ))}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
  },
});

export default HomeScreen;
