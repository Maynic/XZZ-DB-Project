/*!
  _   _  ___  ____  ___ ________  _   _   _   _ ___   
 | | | |/ _ \|  _ \|_ _|__  / _ \| \ | | | | | |_ _| 
 | |_| | | | | |_) || |  / / | | |  \| | | | | || | 
 |  _  | |_| |  _ < | | / /| |_| | |\  | | |_| || |
 |_| |_|\___/|_| \_\___/____\___/|_| \_|  \___/|___|
                                                                                                                                                                                                                                                                                                                                       
=========================================================
* Horizon UI - v1.1.0
=========================================================

* Product Page: https://www.horizon-ui.com/
* Copyright 2022 Horizon UI (https://www.horizon-ui.com/)

* Designed and Coded by Simmmple

=========================================================

* The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

*/

// Chakra imports
import { Box, SimpleGrid } from "@chakra-ui/react";
import ColumnsTable from "views/admin/onetable/components/ColumnsTable";
import {
  visitorColumns,
} from "views/admin/onetable/variables/columnsData";

import React, { Component } from "react";

import axios from "axios";
import { API_URL, } from "constants";


class Onetable extends Component {
  state = {
    visitor: []
  };
  API_Visitor = API_URL + "visitor";

  componentDidMount() {
    this.resetState();
  }

  getVisitors = () => {
    // window.alert(this.API_Visitor);
    axios.get(this.API_Visitor).then(res => this.setState({ visitor: res.data }));
  };

  resetState = () => {
    this.getVisitors();
  };

  render() {
    return (
      <Box pt={{ base: "130px", md: "80px", xl: "80px" }}>
        <SimpleGrid
          mb='20px'
          // columns={{ sm: 1, md: 2 }}
          spacing={{ base: "20px", xl: "20px" }}>
          <ColumnsTable
            columnsData={visitorColumns}
            tableData={this.state.visitor}
            resetState={this.resetState}
          />
          {/* <ColumnsTable
            columnsData={visitorColumns}
            tableData={this.state.visitor}
            resetState={this.resetState}
          /> */}
        </SimpleGrid>
      </Box>
    );
  }
}

export default Onetable;