import React from "react";

import { Icon } from "@chakra-ui/react";
import {
  MdBarChart,
  MdPerson,
  MdHome,
  MdLock,
  MdOutlineShoppingCart,
  MdBusiness,
  MdOutlineAttractions,
  MdPayment,
} from "react-icons/md";
import {
  AiFillCar
} from "react-icons/ai";
import {
  TbBuildingCircus
} from "react-icons/tb";
import {
  HiBuildingStorefront
} from "react-icons/hi2";
import {
  IoTicket
} from "react-icons/io5";
import {
  FaFileInvoiceDollar
} from "react-icons/fa";
// Admin Imports
import MainDashboard from "views/admin/default";
// import NFTMarketplace from "views/admin/marketplace";
// import Profile from "views/admin/profile";
// import DataTables from "views/admin/dataTables";
import OneTable from "views/admin/Visitor";
import Attraction from "views/admin/Attraction";
import Parking from "views/admin/Parking";
import Payment from "views/admin/Payment";
import Show from "views/admin/Show";
import Store from "views/admin/Store";
import Ticket from "views/admin/Ticket";
import StoreOrder from "views/admin/StoreOrder";
// import RTL from "views/admin/rtl";

// Auth Imports
import SignInCentered from "views/auth/signIn";

const routes = [
  {
    name: "Dashboard",
    layout: "/admin",
    path: "/default",
    icon: <Icon as={MdHome} width='20px' height='20px' color='inherit' />,
    component: MainDashboard,
  },


  // {
  //   name: "NFT Marketplace",
  //   layout: "/admin",
  //   path: "/nft-marketplace",
  //   icon: (
  //     <Icon
  //       as={MdOutlineShoppingCart}
  //       width='20px'
  //       height='20px'
  //       color='inherit'
  //     />
  //   ),
  //   component: NFTMarketplace,
  //   secondary: true,
  // },
  // {
  //   name: "Data Tables",
  //   layout: "/admin",
  //   icon: <Icon as={MdBarChart} width='20px' height='20px' color='inherit' />,
  //   path: "/data-tables",
  //   component: DataTables,
  // },
  // {
  //   name: "Profile",
  //   layout: "/admin",
  //   path: "/profile",
  //   icon: <Icon as={MdPerson} width='20px' height='20px' color='inherit' />,
  //   component: Profile,
  // },
  // {
  //   name: "Sign In",
  //   layout: "/auth",
  //   path: "/sign-in",
  //   icon: <Icon as={MdLock} width='20px' height='20px' color='inherit' />,
  //   component: SignInCentered,
  // },
  {
    name: "Visitor",
    layout: "/admin",
    path: "/onetable",
    icon: <Icon as={MdPerson} width='20px' height='20px' color='inherit' />,
    component: OneTable,
  },
  {
    name: "Attraction",
    layout: "/admin",
    path: "/attraction",
    icon: <Icon as={MdOutlineAttractions} width='20px' height='20px' color='inherit' />,
    component: Attraction,
  },
  {
    name: "Parking",
    layout: "/admin",
    path: "/parking",
    icon: <Icon as={AiFillCar} width='20px' height='20px' color='inherit' />,
    component: Parking,
  },
  {
    name: "Payment",
    layout: "/admin",
    path: "/payment",
    icon: <Icon as={MdPayment} width='20px' height='20px' color='inherit' />,
    component: Payment,
  },
  {
    name: "Show",
    layout: "/admin",
    path: "/show",
    icon: <Icon as={TbBuildingCircus} width='20px' height='20px' color='inherit' />,
    component: Show,
  },
  {
    name: "Store",
    layout: "/admin",
    path: "/store",
    icon: <Icon as={HiBuildingStorefront} width='20px' height='20px' color='inherit' />,
    component: Store,
  },
  {
    name: "Ticket",
    layout: "/admin",
    path: "/ticket",
    icon: <Icon as={IoTicket} width='20px' height='20px' color='inherit' />,
    component: Ticket,
  },
  {
    name: "Store Order",
    layout: "/admin",
    path: "/sorder",
    icon: <Icon as={FaFileInvoiceDollar} width='20px' height='20px' color='inherit' />,
    component: StoreOrder,
  },
];

export default routes;
