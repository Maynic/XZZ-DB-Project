import React from "react";
// import {Text} from 'react-native';

// Chakra imports
import { Flex, useColorModeValue } from "@chakra-ui/react";

// Custom components
import { HorizonLogo } from "components/icons/Icons";
import { HSeparator } from "components/separator/Separator";

// const styles = StyleSheet.create({
//   baseText: {
//     fontFamily: 'Cochin',
//   },
//   titleText: {
//     fontSize: 20,
//     fontWeight: 'bold',
//   },
// });

export function SidebarBrand() {
  //   Chakra color mode
  // let logoColor = useColorModeValue("navy.700", "white");

  return (
    <Flex align='center' direction='column'>
      {/* <Text  /> */}
      {/* <Text style={styles.titleText} > */}
      <span style={{ fontWeight: 'bold' }}>Voyage of Amusements</span>
      <span>"\n"</span>

{/* {"Voyage of Amusements"} */}
      {/* </Text> */}
      {/* <HorizonLogo h='26px' w='175px' my='32px' color={logoColor} /> */}
      <HSeparator mb='20px' />
    </Flex>
  );
}

export default SidebarBrand;
